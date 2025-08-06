import http from "k6/http";
import { check, sleep } from "k6";

export let options = {
  vus: 10,
  duration: "30s",
  thresholds: {
    http_req_duration: ["p(95)<500"], // 95% of all requests finish under 500ms
    http_req_failed: ["rate<0.01"], // Less than 1% of requests fail
  },
};

export default function () {
  let res1 = http.get("https://jsonplaceholder.typicode.com/posts/1");
  let res2 = http.get("https://jsonplaceholder.typicode.com/comments/1");

  check(res1, { "post 1 status is 200": (r) => r.status === 200 });
  check(res2, { "comment 1 status is 200": (r) => r.status === 200 });

  sleep(1);
}
