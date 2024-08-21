# MSA & DDD 디자인 패턴

> Initial written at August 21, 2024 <br/>
> last updated at: August 21, 2024


## Current: ver. 1.0.0<br/>

> - FastAPI Container 추가


# 1. 프로그램 (프로젝트) 설명

- 본 프로젝트는 MSA(마이크로서비스 아키텍처)와 DDD(도메인 주도 설계) 원칙을 따르는 방식으로 프로젝트 설계하는 방법을 공부하는 프로젝트 입니다.


# 2. Prerequisite

- 본 프로젝트는 Docker를 사용하므로 `.env.template` 파일을 참고하여 `.env` 파일에 환경 변수값을 작성해주세요.
    ```
    FASTAPI_PORT=호스트 포트
    ```


# 3. 구동 방법

## 3.1. 프로젝트 실행

본 프로젝트는 Docker Compose를 사용하므로 이를 실행시켜주세요.

```shell
(sudo) docker compose up
```

# 4. 디렉토리 및 파일 설명
```
    /project-root
    │
    ├── data/
    │   ├── elasticsearch-data/ (optional for persistent MongoDB storage)
    │   ├── mongodb-data/ (optional for persistent MongoDB storage)
    │   └── mariadb-data/ (optional for persistent MariaDB storage)
    │
    ├── fastapi-service/
    │   ├── .env
    │   ├── .env.template
    │   ├── dockerfile
    │   ├── entrypoint.sh
    │   ├── requirements.txt
    │   ├── venv/
    │   ├── app/
    │   │   ├── main.py
    │   │   ├── models/
    │   │   │   └── search_model.py
    │   │   ├── routers/
    │   │   │   └── search_router.py
    │   │   ├── schemas/
    │   │   │   └── search_schema.py
    │   │   └── services/
    │   │       └── search_service.py
    │   └── config/
    │       ├── config.ini
    │       ├── database.py
    │       └── settings.py
    │
    ├── springboot-service/
    │   ├── Dockerfile
    │   └── src/
    │       ├── main/
    │       │   ├── java/
    │       │   │   └── com/
    │       │   │       └── example/
    │       │   │           └── auth/
    │       │   │               ├── controller/
    │       │   │               │   └── AuthController.java
    │       │   │               ├── model/
    │       │   │               │   └── User.java
    │       │   │               ├── repository/
    │       │   │               │   └── UserRepository.java
    │       │   │               ├── service/
    │       │   │               │   └── AuthService.java
    │       │   │               └── SpringbootServiceApplication.java
    │       │   └── resources/
    │       │       ├── application.properties
    │       │       └── application.yml
    │       └── test/
    │           └── java/
    │               └── com/
    │                   └── example/
    │                       └── auth/
    │                           └── AuthServiceTests.java
    │
    ├── .gitignore
    ├── docker-compose.yml
    └── README.md
```