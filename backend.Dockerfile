FROM rockylinux/rockylinux:9

RUN dnf -y update && dnf -y install gcc-gfortran python3-pip

RUN mkdir /backend
COPY main.py /backend
COPY BouguerGrid /backend
COPY DEMGrid /backend
COPY FAGrid /backend
COPY GCGGrid /backend
COPY GDGrid /backend

RUN mkdir /backend/fortran_interop
COPY fortran_interop /backend/fortran_interop


RUN pip install fastapi[all]

EXPOSE 8008
CMD uvicorn main:app --host 0.0.0.0 --port 8008 --app-dir /backend
