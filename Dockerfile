FROM python:alpine

COPY search_path.sh extract_path_value.py config.txt /tmp/
RUN chmod +x \
    /tmp/search_path.sh \
    /tmp/extract_path_value.py

ENTRYPOINT ["sh"]