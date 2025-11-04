import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailSender:
    def __init__(self, smtp_server, smtp_port, username, password, use_tls=True):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
        self.use_tls = use_tls

    def send_html_email(self, to_email, subject, html_content, from_email=None):
        if from_email is None:
            from_email = self.username

        # Crear el mensaje
        msg = MIMEMultipart('alternative')
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Adjuntar el contenido HTML
        html_part = MIMEText(html_content, 'html')
        msg.attach(html_part)

        try:
            # Conectar al servidor SMTP
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            if self.use_tls:
                server.starttls()
            server.login(self.username, self.password)
            text = msg.as_string()
            server.sendmail(from_email, to_email, text)
            server.quit()
            print("Correo enviado exitosamente.")
        except Exception as e:
            print(f"Error al enviar el correo: {e}")


    def mail_template(self, title, rows = ""):
        # Renderizar la plantilla con el contexto proporcionado
       
        html_content = '<!DOCTYPE html>'
        html_content += '<html lang="en">'
        html_content += '<head>'
        html_content += '  <meta charset="utf-8" />'
        html_content += '  <meta name="viewport" content="width=device-width, initial-scale=1" />'
        html_content += f'  <title>{title}</title>'
        html_content += '  <!-- Opcional: Inter. Muchos clientes usarán el fallback -->'
        html_content += '  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap" rel="stylesheet" />'
        html_content += '  <style>'
        #/* ===== Reset básico y tipografía ===== */
        html_content += '    html, body {'
        html_content += '      margin: 0 !important;'
        html_content += '      padding: 0 !important;'
        html_content += '      height: 100% !important;'
        html_content += '      width: 100% !important;'
        html_content += '      -webkit-text-size-adjust: 100%;'
        html_content += '      -ms-text-size-adjust: 100%;'
        html_content += '    }'
        html_content += '    body {'
        html_content += '      background: #f8fafc;'
        html_content += '      font-family: Inter, Arial, Helvetica, sans-serif;'
        html_content += '      color: #1e293b;'
        html_content += '      line-height: 1.5;'
        html_content += '    }'
        html_content += '    img { border: 0; outline: none; text-decoration: none; height: auto; max-width: 100%; }'
        html_content += '    a { text-decoration: none; }'
        html_content += '    table { border-collapse: collapse; }'
        #/* ===== Layout ===== */
        html_content += '    .wrapper { width: 100%; background: #f8fafc; }'
        html_content += '    .container { width: 100%; max-width: 600px; margin: 0 auto; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; overflow: hidden; }'
        html_content += '    .section { padding: 24px; }'
        html_content += '    .header { display: flex; align-items: center; gap: 12px; border-bottom: 1px solid #e2e8f0; }'
        html_content += '    .brand { font-weight: 700; font-size: 18px; }'
        html_content += '    .title { font-size: 24px; font-weight: 800; margin: 0 0 4px; color: #0f172a; }'
        html_content += '    .subtitle { font-size: 14px; color: #64748b; margin: 0; }'
        html_content += '    .paragraph { font-size: 16px; margin: 0 24px 16px; }'
        #/* ===== Cards métricas ===== */
        html_content += '    .cards { padding: 0 24px 8px; }'
        html_content += '    .card {'
        html_content += '      border: 1px solid #e2e8f0;'
        html_content += '      background: #e6f2ff;'
        html_content += '      border-radius: 10px;'
        html_content += '      padding: 14px 16px;'
        html_content += '      margin-bottom: 12px;'
        html_content += '    }'
        html_content += '    .metric-label { font-size: 12px; color: #64748b; margin: 0 0 4px; }'
        html_content += '    .metric-value { font-size: 20px; font-weight: 700; margin: 0; color: #0f172a; }'
        html_content += '    .metric-change { font-size: 12px; font-weight: 600; margin: 6px 0 0; }'
        html_content += '    .green { color: #16a34a; }'
        html_content += '    .red { color: #dc2626; }'
        # /* ===== CTA ===== */
        html_content += '    .cta-wrap { padding: 16px 24px 24px; }'
        #    /* Nota: estilos inline en el <a> para máxima compatibilidad */
        #/* ===== Footer ===== */
        html_content += '    .footer { border-top: 1px solid #e2e8f0; padding: 24px; color: #64748b; font-size: 12px; }'
        html_content += '    .mt-8 { margin-top: 8px; }'

        #/* ===== Mobile tweaks (opcional) ===== */
        html_content += '    @media only screen and (max-width: 620px) {'
        html_content += '      .section, .cards, .cta-wrap { padding-left: 16px; padding-right: 16px; }'
        html_content += '      .paragraph { margin-left: 16px; margin-right: 16px; }'
        html_content += '      .title { font-size: 22px; }'
        html_content += '    }'
        html_content += '  </style>'
        html_content += '</head>'
        html_content += '<body>'
        html_content += '  <center class="wrapper">'
        html_content += '    <table role="presentation" width="100%" cellpadding="0" cellspacing="0">'
        html_content += '      <tr>'
        html_content += '        <td style="padding:16px;">'
        html_content += '          <table role="presentation" class="container" cellpadding="0" cellspacing="0">'
        #                            <!-- Header -->'
        html_content += '            <tr>'
        html_content += '              <td class="section">'
        html_content += '                <div class="header">'
        #                                  <!-- Simple icon (evitamos fuentes de íconos) -->
        html_content += '                  <div aria-hidden="true" style="font-size:24px; line-height:1;">◔</div>'
        html_content += '                  <div class="brand">AGIOTECH DE MEXICO S.A. DE C.V.</div>'
        html_content += '                </div>'
        html_content += '              </td>'
        html_content += '            </tr>'

        #    <!-- Título -->
        html_content += '            <tr>'
        html_content += '              <td class="section" style="padding-top:12px;">'
        html_content += '                <h1 class="title">Recordatorio de Órdenes Pendientes</h1>'
        html_content += F'                <p class="subtitle">Generado el: {datetime.now()}</p>'
        html_content += '              </td>'
        html_content += '            </tr>'


        #<!-- Recordatorio de órdenes pendientes -->
        html_content += '            <tr>'
        html_content += '              <td class="section" style="padding-top:12px;">'
        html_content += F'                <p class="subtitle">Comunicación interna: Esta notificación es informativa. Atiende o actualiza el estado de tus pedidos.</p>'
        html_content += '              </td>'
        html_content += '            </tr>'


        html_content += '            <tr>'
        html_content += '              <td class="section" style="padding-top:12px;">'

          
        html_content += '                <p style="margin:0 0 8px 0;">Hola,</p>'
        html_content += '                <p style="margin:0 0 16px 0;">Estas son tus órdenes ONE STOP pendientes por agendar cita:</p>'
          
        html_content += '                <table border="0" cellpadding="6" cellspacing="0" style="border-collapse:collapse;width:100%;background:#1F1F1F;color:#EDEDED;">'
        html_content += '                 <thead>'
        html_content += '                   <tr style="text-align:left;border-bottom:1px solid #444;">'
        html_content += '                     <th>Referencia de reparación</th>'
        html_content += '                     <th>Cliente</th>'
        html_content += '                     <th>Producto a reparar</th>'
        html_content += '                     <th>Lote /Número de serie</th>'
        html_content += '                     <th>Fecha GSPN</th>'
        html_content += '                     <th>Creado el</th>'
        html_content += '                     <th>Status</th>'
        html_content += '                     <th></th>'
        html_content += '                   </tr>'
        html_content += '                 </thead>'
        html_content += '                 <tbody>'
        #html_content += f'                  {.join(rows)}'
        html_content += '                 </tbody>'
        html_content += '                </table>'
        html_content += '              </td>'
        html_content += '            </tr>'
      
        #    <!-- Footer -->
        html_content += '            <tr>'
        html_content += '              <td class="footer">'
        html_content += '                <div><strong>AGIOTECH DE MEXICO </strong> <br />'
        html_content += '                +52 33 3627 7575 | contacto@agiotech.com | https://www.agiotech.com  </div>'
        html_content += '                <div class="mt-8">This is an automated report generated fot IT Developemt Team.</div>'
        html_content += '              </td>'
        html_content += '            </tr>'

        html_content += '          </table>'
        html_content += '        </td>'
        html_content += '      </tr>'
        html_content += '    </table>'
        html_content += '  </center>'
        html_content += '</body>'
        html_content += '</html>'

        return html_content
        '''
        #    <!-- Intro -->
            <tr>
              <td>
                <p class="paragraph">
                  Hello Team, here is your performance snapshot for the past week.
                </p>
              </td>
            </tr>

        #    <!-- Métricas -->
            <tr>
              <td class="cards">
                <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
                  <tr>
                    <td class="card">
                      <p class="metric-label">Revenue</p>
                      <p class="metric-value">$45,230</p>
                      <p class="metric-change green">+5.2%</p>
                    </td>
                  </tr>
                  <tr>
                    <td class="card">
                      <p class="metric-label">Tasks Completed</p>
                      <p class="metric-value">128</p>
                      <p class="metric-change green">+12%</p>
                    </td>
                  </tr>
                  <tr>
                    <td class="card">
                      <p class="metric-label">Customer Satisfaction</p>
                      <p class="metric-value">95%</p>
                      <p class="metric-change red">-1.5%</p>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>

        #    <!-- CTA -->
            <tr>
              <td class="cta-wrap">
                <a href="#"
                   style="display:inline-block;background:#007BFF;color:#ffffff;font-weight:600;font-size:16px;line-height:1;border-radius:10px;padding:12px 20px;text-align:center;">
                  View Full Report in Odoo
                </a>
              </td>
            </tr>
'''         