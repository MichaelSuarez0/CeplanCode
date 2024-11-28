import streamlit as st
import imaplib
import email
import re
import pandas as pd
from email.header import decode_header
from datetime import datetime

# Función para extraer y convertir la fecha al formato DD/MM/YYYY
def extract_date(date_str):
    """Extraer solo la fecha en formato DD/MM/YYYY."""
    match = re.search(r"\d{1,2} \w{3} \d{4}", date_str)
    if match:
        date_obj = datetime.strptime(match.group(0), "%d %b %Y")
        return date_obj.strftime("%d/%m/%Y")
    else:
        raise ValueError(f"No se pudo procesar la fecha: {date_str}")

# Función para separar Nombre y Correo
def split_remitente(remitente):
    """Divide el remitente en nombre y correo electrónico."""
    match = re.search(r"<(.+)>", remitente)
    if match:
        correo = match.group(1)  # Lo que está dentro de <>
        nombre = remitente.split("<")[0].strip().replace('"', '')  # Eliminar comillas
        return nombre, correo
    else:
        return remitente.strip().replace('"', ''), ""

# Función principal de Streamlit
def main():
    st.title("Consulta de Correos IMAP")

    # Inputs de usuario: campos para IMAP_SERVER, USERNAME, PASSWORD y IMAP_PORT
    imap_server = st.text_input("Servidor IMAP", value="imap.gmail.com")  # El valor por defecto es para Gmail
    username = st.text_input("Correo electrónico (Username)")
    password = st.text_input("Contraseña", type="password")
    imap_port = st.number_input("Puerto IMAP", value=993, step=1)  # Puerto predeterminado es 993 para IMAP seguro
    
    # Inputs de fecha
    start_date = st.date_input("Fecha de inicio", value=datetime(2024, 10, 21))
    end_date = st.date_input("Fecha de fin", value=datetime(2024, 11, 5))

    if st.button("Consultar Correos"):
        if not username or not password or not imap_server:
            st.error("Por favor ingrese todos los campos requeridos.")
            return

        try:
            # Conectar al servidor IMAP con los parámetros proporcionados
            mail = imaplib.IMAP4_SSL(imap_server, imap_port)
            mail.login(username, password)
            st.success("Conexión exitosa al servidor IMAP")
        except TimeoutError:
            st.error("Error: El servidor no respondió. Verifica tu conexión y la configuración del servidor IMAP.")
            return
        except imaplib.IMAP4.error:
            st.error("Error: No se pudo iniciar sesión. Verifica tu usuario y contraseña.")
            return
        except Exception as e:
            st.error(f"Error inesperado: {e}")
            return

        # Seleccionar la bandeja de entrada
        mail.select("inbox")
        status, messages = mail.search(None, f"SINCE {start_date.strftime('%d-%b-%Y')} BEFORE {end_date.strftime('%d-%b-%Y')}")
        if status != "OK":
            st.error("Error al buscar los correos.")
            mail.logout()
            return

        email_ids = messages[0].split()

        email_data = []

        # Descargar y procesar los correos
        for email_id in email_ids:
            status, msg_data = mail.fetch(email_id, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])

                    # Decodificar el Asunto
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        try:
                            subject = subject.decode(encoding if encoding else "utf-8")
                        except (LookupError, UnicodeDecodeError):
                            subject = subject.decode("latin-1", errors="ignore")

                    # Decodificar el remitente y destinatario
                    def decode_mime_header(header):
                        decoded_parts = decode_header(header)
                        decoded_string = ""
                        for part, enc in decoded_parts:
                            if isinstance(part, bytes):
                                try:
                                    decoded_string += part.decode(enc if enc else "utf-8")
                                except (LookupError, UnicodeDecodeError):
                                    decoded_string += part.decode("latin-1", errors="ignore")
                            else:
                                decoded_string += part
                        return decoded_string

                    from_decoded = decode_mime_header(msg.get("From"))
                    to_decoded = decode_mime_header(msg.get("To"))

                    # Usar la función para separar nombre y correo
                    nombre, correo = split_remitente(from_decoded)

                    # Obtener y procesar la fecha
                    date = msg.get("Date")
                    try:
                        parsed_date = extract_date(date)
                    except ValueError:
                        continue

                    # Procesar el contenido del correo
                    body = None
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = part.get("Content-Disposition")

                            # Asegurarnos de que Content-Disposition no sea None
                            if content_type == "text/plain" and (content_disposition is None or "attachment" not in content_disposition):
                                try:
                                    body = part.get_payload(decode=True).decode("utf-8")
                                except UnicodeDecodeError:
                                    body = part.get_payload(decode=True).decode("latin-1", errors="ignore")
                                break
                    else:
                        try:
                            body = msg.get_payload(decode=True).decode("utf-8")
                        except UnicodeDecodeError:
                            body = msg.get_payload(decode=True).decode("latin-1", errors="ignore")

                    if body:
                        body = re.sub(r"(\n\s*){2,}", "\n", body.strip())

                    # Agregar los datos al listado
                    email_data.append({
                        "Asunto": subject,
                        "Nombre": nombre,
                        "Correo": correo,
                        "Remitente": from_decoded,
                        "Destinatario": to_decoded,
                        "Fecha": parsed_date,
                        "Cuerpo del mensaje": body
                    })

        # Crear un DataFrame a partir de los datos
        df = pd.DataFrame(email_data)

        if not df.empty:
            # Mostrar los correos únicos y repetidos
            st.subheader("Correos encontrados")
            st.write(df)

            # Identificar correos repetidos
            duplicados = df[df.duplicated(subset=["Correo"], keep=False)]
            correos_unicos = df.drop_duplicates(subset=["Correo"])

            st.write(f"\nCantidad de correos únicos: {len(correos_unicos)}")
            st.write(f"Cantidad de correos repetidos: {len(duplicados)}")

            # Descargar los datos como CSV
            csv = correos_unicos.to_csv(index=False)
            st.download_button("Descargar Correos Únicos", csv, "correos_unicos.csv", "text/csv")
        else:
            st.warning("No se encontraron correos para este rango de fechas.")

        mail.logout()

if __name__ == "__main__":
    main()
