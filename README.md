Também é possível usar a PyRe para resolver grandes listas de IPs usando o seguinte one-liner:

for host in $(cat lista-ip.txt);do python pyre.py >> output.txf;done
