Kafka starts:
docker-compose up -d

Build the Docker image:
docker build -t kafka-example .

Producer executes:
docker run --network="host" kafka-example --mode producer

Executes the consumer:
docker run --network="host" kafka-example --mode consumer