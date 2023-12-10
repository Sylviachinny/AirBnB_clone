<h1>0x00. AirBnB clone - The console</h1>

<strong>Concepts</strong>
For this project, we expect you to look at these concepts: </br>
[Python packages](https://intranet.alxswe.com/concepts/66)</br>
[AirBnB](https://intranet.alxswe.com/concepts/74)</br>

<img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231210%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231210T185729Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=10dd10676962c4a5ef6d9a2bc18e106aadc853816419326a0983477327e477e5" width="100%">
</br>

<h3>Background Context</h3>
<strong>Welcome to the AirBnB clone project!</strong>
Before starting, please read the AirBnB concept page.</br>
<strong>First step: Write a command interpreter to manage your AirBnB objects.</strong>
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…</br>

Each task is linked and will help you to:</br>

put in place a parent class (called <strong> BaseModel,</strong>) to take care of the initialization, serialization and deserialization of your future instances </br>
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file </br>
create all classes used for AirBnB <strong> (User, State, City, Place…) </strong> that inherit from <strong> BaseModel  </strong></br>
create the first abstracted storage engine of the project: File storage. </br>
create all unittests to validate all our classes and storage engine </br>

<h3>What’s a command interpreter?</h3>
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:</br>

Create a new object (ex: a new User or a new Place)</br>
Retrieve an object from a file, a database etc…</br>
Do operations on objects (count, compute stats, etc…)</br>
Update attributes of an object</br>
Destroy an object</br>

<h4>Resources</h4>
[cmd module](https://intranet.alxswe.com/rltoken/8ecCwE6veBmm3Nppw4hz5A) </br>
[cmd module in depth](https://intranet.alxswe.com/rltoken/uEy4RftSdKypoig9NFTvCg) </br>
[uuid module](https://intranet.alxswe.com/rltoken/KfL9TqwdI69W6ttG6gTPPQ) </br>
[datetime](https://intranet.alxswe.com/rltoken/1d8I3jSKgnYAtA1IZfEDpA) </br>
[unittest module](https://intranet.alxswe.com/rltoken/IlFiMB8UmqBG2CxA0AD3jA) </br>
[args/kwargs](https://intranet.alxswe.com/rltoken/C_a0EKbtvKdMcwIAuSIZng) </br>
[python test cheatsheet](https://intranet.alxswe.com/rltoken/tgNVrKKzlWgS4dfl3mQklw) </br>
[cmd module wiki page](https://intranet.alxswe.com/rltoken/EvcaH9uTLlauxuw03WnkOQ) </br>
[python unittest](https://intranet.alxswe.com/rltoken/begh14KQA-3ov29KvD_HvA) </br>

<strong>Learning Objectives</strong>
At the end of this project, you are expected to be able to explain to anyone, without the help of Google: <br>
