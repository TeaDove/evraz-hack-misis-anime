const backendUrl = "http://158.160.13.117:8000"

const fetchExhausters = async () => {
  let resp = await fetch(`${backendUrl}/exhausters`)
  let data = await resp.json()

  return data["exhausters"]
}

const fetchExhausterInfo = async (exhausterId) => {
  let resp = await fetch(`${backendUrl}/exhausters/${exhausterId}`)
  let data = await resp.json()

  return data["exhauster"]
}

export {fetchExhausters, fetchExhausterInfo}
