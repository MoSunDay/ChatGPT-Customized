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