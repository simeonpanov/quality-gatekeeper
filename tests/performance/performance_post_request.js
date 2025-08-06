import http from "k6/http";
import { check } from "k6";

export let options = {
  vus: 5,
  duration: "10s",
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
