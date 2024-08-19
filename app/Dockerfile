FROM python

WORKDIR /app

RUN git clone https://github.com/sarthak0401/sb-career-v3.git .

RUN git checkout containerization 
 
RUN pip3 install -r requirements.txt

ENV FLASK_APP=app.py  

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
