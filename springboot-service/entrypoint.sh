#!/bin/bash
# entrypoint.sh

# Print environment variables (optional, for debugging)
echo "Starting Spring Boot application..."

# Run the Spring Boot application
exec java -jar /springboot-app/build/libs/springboot-service-0.0.1-SNAPSHOT.jar