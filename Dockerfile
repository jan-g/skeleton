ARG python=3.11
FROM python:$python AS build

WORKDIR /src

# Split this because requirements installation can be cacheable
RUN pip install -U pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN pip install .

FROM python:$python AS run
# Annoyingly, the python:3.11 image has a /usr/local/lib/python3.9 directory knocking around (?)
COPY --from=build /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=build /usr/local/bin /usr/local/bin

ENTRYPOINT ["/usr/local/bin/cmd"]
CMD []
