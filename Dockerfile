# 
FROM python:3.9

# 
WORKDIR /

# 
COPY ./requirements.txt /requirements.txt

# 
RUN sudo apt update && sudo apt install -y ffmpeg

#
RUN pip install --no-cache-dir --upgrade -r /requirements.txt

# 
COPY ./ /

# 

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]