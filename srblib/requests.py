def debug_res(res): # input is response of a requests module.
	req = res.request
	print('{}\n{}\n{}\n\n{}\n\n{}\n{}\n{}\n{}\n\n{}\n'.format(
		'-----------Request-----------',
		req.method + ' ' + req.url,
		'\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
		req.body,
		'-----------Response-----------',
		"Status : " + str(res.status_code),
		"Encoding : " + str(res.encoding),
		'\r\n'.join('{}: {}'.format(k, v) for k, v in res.headers.items()),
		res.text,
	))