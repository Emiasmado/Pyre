Também é possível usar a PyRe para resolver grandes listas de IPs usando o seguinte one-liner:

ISSO AQUI É PRA LINUX!!!:
for host in $(cat lista-ip.txt);do python pyre.py >> output.txf;done
