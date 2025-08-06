import http from "k6/http";
import { check } from "k6";

export let options = {
  vus: 5,
  duration: "10s",
  thresholds: {
    http_req_duration: ["p(95)<500"],
    http_req_failed: ["rate<0.01"],
  },
};

export default function () {
  let url = "https://jsonplaceholder.typicode.com/posts";
  let payload = JSON.stringify({
    title: "foo",
    body: "bar",
    userId: 1,
  });

  let params = {
    headers: {
      "Content-Type": "application/json",
    },
  };

  let res = http.post(url, payload, params);
  check(res, {
    "status is 201": (r) => r.status === 201,
  });
}
