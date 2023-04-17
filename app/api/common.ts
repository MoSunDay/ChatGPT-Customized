import { NextRequest } from "next/server";

const OPENAI_URL = "127.0.0.1:8080/api/v1/gpt";
const DEFAULT_PROTOCOL = "http";
export const PROTOCOL = process.env.PROTOCOL ?? DEFAULT_PROTOCOL;
export const BASE_URL = process.env.BASE_URL ?? OPENAI_URL;
export const BASE_API = process.env.BASE_API ?? OPENAI_URL;

export async function requestOpenai(req: NextRequest) {
  const apiKey = req.headers.get("token");
  const openaiPath = req.headers.get("path");

  let baseUrl = BASE_URL;
  console.log("[debug] ", baseUrl);

  if (!baseUrl.startsWith("http")) {
    baseUrl = `${PROTOCOL}://${baseUrl}`;
  }

  console.log("[Proxy] ", openaiPath);
  console.log("[Base Url]", baseUrl);

  const requestHeaders = new Headers(req.headers);
  requestHeaders.set("Content-Type", "application/json");
  requestHeaders.set("Authorization", `Bearer ${apiKey}`);

  return fetch(`${baseUrl}/${openaiPath}`, {
    headers: requestHeaders,
    method: req.method,
    body: req.body,
  });
}
