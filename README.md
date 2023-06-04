Camunda utils
================================

A utils worker for currently missing parts...

Configure
---------

Set a virtual python environment for version 3.7.10 and install requirements:

```bash
pip install -r requirements.txt 
```

Run locally
-----------

If you have a local/docker-compose Zeebe running locally you can run/debug with:

```bash
python index.py
```

Build with Docker
-----------------

```bash
docker build -t docker.pkg.github.com/teode/camunda-utils-worker:v1.0.0 .
```

Make a Github package
---------------------

```bash
docker push docker.pkg.github.com/teode/camunda-utils-worker:v1.0.0
```

Else get it from Docker hub:

Or download from: https://hub.docker.com/r/teode/camunda-utils--worker

Usage
-----

Example BPMN with service task:

 ```xml
 <bpmn:serviceTask id="utils-" name="Turn a JSON string into an object">
   <bpmn:extensionElements>
     <zeebe:taskDefinition type="utils-json-string-to-object" />
   </bpmn:extensionElements>
 </bpmn:serviceTask>
 ```

The worker is currently registered for `utils-json-string-to-object` tasks (more to come):
* required variables:
  * `jsonString` - the JSON string to deserialize
* jobs are completed with a `response` object containing a deserialized JSON object