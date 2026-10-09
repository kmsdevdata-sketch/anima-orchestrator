# Orchestrator

로컬 PC에서 Cockpit/Codex의 **제한된 요청**과 ESP32 사이에 놓이는 제어 경계다. 현재는 구현 전이다. 구조 기준은 [`planning/platform-foundations.md`](../../planning/platform-foundations.md)와 [`shared/protocol/README.md`](../../shared/protocol/README.md)를 따른다.

첫 구현은 [제어 계약 v0.1](../../shared/protocol/v0.md)의 HTTP JSON 명령·조회와 SSE 이벤트를 대상으로 한다. 명령 검증, 중복 요청 방지, 단일 주행/충돌 처리, 만료, 정지 우선 처리, 상태 조회, 이벤트 기록을 모의 장치로 검증한 뒤 ESP32 어댑터를 붙인다. 저장소와 런타임 언어는 구현 시 결정한다.

Cockpit에 로봇 IP나 모터 핀을 노출하지 않는다. 로그에서 `요청`, `장치 수신`, `실제 이동`을 같은 결과로 합치지 않는다. Orchestrator 자체가 죽거나 네트워크가 끊겨도 ESP32의 로컬 정지 장치가 동작해야 한다.
