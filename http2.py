try:
    import socket, ssl, argparse, platform, os
    from urllib.parse import urlparse
except ImportError as eImp:
    print(f"Ocurrió el error: {eImp}")

def ValidarSOLimpiar():
  sistema= platform.system()
  if sistema== "Windows":
    return "cls"
  else:
    return "clear"

socket.setdefaulttimeout(5)

def check_http2(domain_name):
 try:
  HOST = urlparse(domain_name).netloc
  PORT = 443

  ctx = ssl.create_default_context()
  ctx.set_alpn_protocols(['h2', 'spdy/3', 'http/1.1'])

  conn = ctx.wrap_socket(
   socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_hostname=HOST)
  conn.connect((HOST, PORT))

  pp = conn.selected_alpn_protocol()

  if pp == "h2":
   return "The site has http2 enabled"
  else:
   return "The site doesn´t has http2 enabled"
 except Exception as e:
  print(e)


parser = argparse.ArgumentParser()
parser.add_argument("domain", help="display a square of a given number",
                    type=str)
args = parser.parse_args()

if __name__== "__main__":
  os.system(ValidarSOLimpiar())
  print(check_http2(args.domain))