import { NextRequest, NextResponse } from "next/server";
import { getServerSideConfig } from "./app/config/server";
import md5 from "spark-md5";

export const config = {
  matcher: ["/api/openai", "/api/chat-stream"],
};

// const serverConfig = getServerSideConfig();

export function middleware(req: NextRequest) {
  return NextResponse.next({
    request: {
      headers: req.headers,
    },
  });
}

// curl 'http://9.134.237.219:20234/api/chat-stream' \
  // -H 'Accept: */*' \
  // -H 'Accept-Language: en-US,en;q=0.9' \
  // -H 'Connection: keep-alive' \
  // -H 'Content-Type: application/json' \
  // -H 'Origin: http://9.134.237.219:20234' \
  // -H 'Referer: http://9.134.237.219:20234/' \
  // -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36' \
  // -H 'access-code;' \
  // --data-raw '{"messages":[{"role":"user","content":"123123"}],"stream":true,"model":"gpt-4","temperature":0.9,"presence_penalty":0.8}' \
  // --compressed \
  // --insecure