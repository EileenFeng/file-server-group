# All protection mechanisms on, except stack protection
fs: server.c
	gcc -o fs server.c -g -fno-stack-protector


