#FROM astrocrpublic.azurecr.io/runtime:3.0-6

FROM quay.io/astronomer/astro-runtime:10.5.0
RUN pip install -r requirements.txt
