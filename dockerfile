FROM conda/miniconda3

RUN pip install joblib sklearn flask

COPY . .

ENV MODEL_PATH='model'

EXPOSE 5000

CMD [ "python", "./server.py" ]
