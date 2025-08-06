import http from "k6/http";
import { check } from "k6";

export let options = {
  stages: [
    { duration: "10s", target: 5 },
    { duration: "10s", target: 10 },
    { duration: "10s", target: 0 },
  ],
  thresholds: {
    http_req_duration: ["p(95)<500"], // 95% of requests must finish under 500ms
    http_req_failed: ["rate<0.01"], // Less than 1% requests should fail
  },
};

export default function () {
  let res = http.get("https://jsonplaceholder.typicode.com/posts/2");
  check(res, { "status is 200": (r) => r.status === 200 });
}
