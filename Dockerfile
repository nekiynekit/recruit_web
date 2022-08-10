FROM python:3.9.7
WORKDIR /recruit_web
COPY requirement.txt /recruit_web
RUN pip install --upgrade pip -r requirements.txt
COPY . /recruit_web
EXPOSE 5000