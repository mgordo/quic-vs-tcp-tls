# quic-vs-tcp-tls
Tests and scripts to compare performance of quic vs tcp+tls1.2

This small project contains several scripts to measure performance of tcp+tlsv1.2 VS quic, Google's UDP based protocol.
The project sets a quic server and a quic client, and uses netem and iproute2 to send a pseudo-random file (so as to avoid compression techniques) from the server to the client. The same is done for a tcp server (Apache) and a tcp client (using wget)
The network is simulated under different parameters, which can be changed at will. Default values are:

•	Network delay (ms): 10, 20, 40, 60, 80, 100, or 120

•	Packet loss(%): 0, 2.5 or 5

•	Available bandwidth(Mbps): 1, 40 or 100

Additionally, we test the response to a sudden bandwidth decrease to 10% of the original bandwidth, this tests are called "spike" tests and only show the effect and recovery of said decrease.

Our measurements were taken in October 15, with the following specifications:

Computer:	Acer Aspire Travelmate B113

CPU:	Intel Pentium 2117U 1.80 GHz

RAM:	4GB DDR3 1600 MHz

OS:	Ubuntu 14.04.3 (Gnome) , 3.13.0-43-generic kernel

QUIC server:	QUIC test server, Chromium 47.0.2517.0 (64-bit)

QUIC client:	Browser, Chromium 47.0.2517.0 (64-bit)

HTTPS server:	Apache/2.4.7 (Ubuntu), configured for TLS1.2

HTTPS client:	GNU Wget 1.15

Network Simulation:	Iproute2 package, "tc netem" and "tc tbf"

Test file generation:	dd if=/dev/urandom of=testfile bs=2M count=16

Packet Capture:	tcpdump version 4.5.1, libpcap version 1.5.3

Matplotlib version:	1.4.0

Python version:	2.7.8

The results are stored in the /plots folder.

After setting up the servers and clients both for quic and tcp, you should run the scripts in the following order: script.py, preprocess.py, averaging.py, avgspikes.py, plotting.py, plottingts.py.
You can change in the scripts the relevant paths to the folders.
You can find information at how to set up a quic test server and test clients at www.chromium.org

Authors: M. Gordo and N. Tatsis
