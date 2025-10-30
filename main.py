/home/yisak/PycharmProjects/X_bot_project_v1/.venv/bin/python /home/yisak/PycharmProjects/X_bot_project_v1/.venv/test_2.py 
Enter the title or the author of the name: andrej karpathy
[['Good Vibrations? A Qualitative Study of Co-Creation, Communication, Flow, and Trust in Vibe Coding', 'https://arxiv.org/pdf/2509.12491'], ['GPT-4o System Card', 'https://arxiv.org/pdf/2410.21276'], ['ART: Actually Robust Training', 'https://arxiv.org/pdf/2408.16285'], ['PixelCNN++: Improving the PixelCNN with Discretized Logistic Mixture Likelihood and Other Modifications', 'https://arxiv.org/pdf/1701.05517'], ['DenseCap: Fully Convolutional Localization Networks for Dense Captioning', 'https://arxiv.org/pdf/1511.07571'], ['Visualizing and Understanding Recurrent Networks', 'https://arxiv.org/pdf/1506.02078'], ['Deep Visual-Semantic Alignments for Generating Image Descriptions', 'https://arxiv.org/pdf/1412.2306'], ['ImageNet Large Scale Visual Recognition Challenge', 'https://arxiv.org/pdf/1409.0575'], ['Deep Fragment Embeddings for Bidirectional Image Sentence Mapping', 'https://arxiv.org/pdf/1406.5679']]
1: Good Vibrations? A Qualitative Study of Co-Creation, Communication, Flow, and Trust in Vibe Coding
2: GPT-4o System Card
3: ART: Actually Robust Training
4: PixelCNN++: Improving the PixelCNN with Discretized Logistic Mixture Likelihood and Other Modifications
5: DenseCap: Fully Convolutional Localization Networks for Dense Captioning
6: Visualizing and Understanding Recurrent Networks
7: Deep Visual-Semantic Alignments for Generating Image Descriptions
8: ImageNet Large Scale Visual Recognition Challenge
9: Deep Fragment Embeddings for Bidirectional Image Sentence Mapping
Enter the one you want to summarize: 9
Download progress: 0.8%
Download progress: 1.7%
Download progress: 2.5%
Download progress: 3.4%
Download progress: 4.2%
Download progress: 5.1%
Download progress: 5.9%
Download progress: 6.8%
Download progress: 7.6%
Download progress: 8.5%
Download progress: 9.3%
Download progress: 10.2%
Download progress: 11.0%
Download progress: 11.9%
Download progress: 12.7%
Download progress: 13.6%
Download progress: 14.4%
Download progress: 15.3%
Download progress: 16.1%
Download progress: 16.9%
Download progress: 17.8%
Download progress: 18.6%
Download progress: 19.5%
Download progress: 20.3%
Download progress: 21.2%
Download progress: 22.0%
Download progress: 22.9%
Download progress: 23.7%
Download progress: 24.6%
Download progress: 25.4%
Download progress: 26.3%
Download progress: 27.1%
Download progress: 28.0%
Download progress: 28.8%
Download progress: 29.7%
Download progress: 30.5%
Download progress: 31.4%
Download progress: 32.2%
Download progress: 33.0%
Download progress: 33.9%
Download progress: 34.7%
Download progress: 35.6%
Download progress: 36.4%
Download progress: 37.3%
Download progress: 38.1%
Download progress: 39.0%
Download progress: 39.8%
Download progress: 40.7%
Download progress: 41.5%
Download progress: 42.4%
Download progress: 43.2%
Download progress: 44.1%
Download progress: 44.9%
Download progress: 45.8%
Download progress: 46.6%
Download progress: 47.5%
Download progress: 48.3%
Download progress: 49.1%
Download progress: 50.0%
Download progress: 50.8%
Download progress: 51.7%
Download progress: 52.5%
Download progress: 53.4%
Download progress: 54.2%
Download progress: 55.1%
Download progress: 55.9%
Download progress: 56.8%
Download progress: 57.6%
Download progress: 58.5%
Download progress: 59.3%
Download progress: 60.2%
Download progress: 61.0%
Download progress: 61.9%
Download progress: 62.7%
Download progress: 63.6%
Download progress: 64.4%
Download progress: 65.3%
Download progress: 66.1%
Download progress: 66.9%
Download progress: 67.8%
Download progress: 68.6%
Download progress: 69.5%
Download progress: 70.3%
Download progress: 71.2%
Download progress: 72.0%
Download progress: 72.9%
Download progress: 73.7%
Download progress: 74.6%
Download progress: 75.4%
Download progress: 76.3%
Download progress: 77.1%
Traceback (most recent call last):
  File "/app/lib/python3.11/site-packages/urllib3/response.py", line 444, in _error_catcher
    yield
  File "/app/lib/python3.11/site-packages/urllib3/response.py", line 567, in read
    data = self._fp_read(amt) if not fp_closed else b""
           ^^^^^^^^^^^^^^^^^^
  File "/app/lib/python3.11/site-packages/urllib3/response.py", line 533, in _fp_read
    return self._fp.read(amt) if amt is not None else self._fp.read()
           ^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/http/client.py", line 473, in read
    s = self.fp.read(amt)
        ^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/socket.py", line 718, in readinto
    return self._sock.recv_into(b)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/ssl.py", line 1314, in recv_into
    return self.read(nbytes, buffer)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/ssl.py", line 1166, in read
    return self._sslobj.read(len, buffer)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TimeoutError: The read operation timed out

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/app/lib/python3.11/site-packages/requests/models.py", line 816, in generate
    yield from self.raw.stream(chunk_size, decode_content=True)
  File "/app/lib/python3.11/site-packages/urllib3/response.py", line 628, in stream
    data = self.read(amt=amt, decode_content=decode_content)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/lib/python3.11/site-packages/urllib3/response.py", line 566, in read
    with self._error_catcher():
  File "/usr/lib/python3.11/contextlib.py", line 158, in __exit__
    self.gen.throw(typ, value, traceback)
  File "/app/lib/python3.11/site-packages/urllib3/response.py", line 449, in _error_catcher
    raise ReadTimeoutError(self._pool, None, "Read timed out.")
urllib3.exceptions.ReadTimeoutError: HTTPSConnectionPool(host='arxiv.org', port=443): Read timed out.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/yisak/PycharmProjects/X_bot_project_v1/.venv/test_2.py", line 39, in <module>
    for chunk in responses.iter_content(chunk_size= 65536):
  File "/app/lib/python3.11/site-packages/requests/models.py", line 822, in generate
    raise ConnectionError(e)
requests.exceptions.ConnectionError: HTTPSConnectionPool(host='arxiv.org', port=443): Read timed out.

Process finished with exit code 1
