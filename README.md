<h1> Aerial Netra </h2>

<h2>Introduction</h2>

<img src="https://i.ibb.co/2dzV1GM/netra.png" alt="netra" border="0">

<p>Aerial Netra is a web platform that help drones transfer and receive data for higher security and better descision making. Basically aerial flight specially UASs or UAVs are much prone to accidents, very much due to unhealthy cloud conditions imprecise, detecting sensors and a lots of other reasons. And a lot of these happenings can simply be solved by transmitting surrounding data to them. And that's our solution, to suppy aerial vehicles with surrounding info from similar aerial vehicles around them. This can also help drone pilots to be aware od their drone's situation and surrounding to make descisions about the flight. </p>

<h2>Basic Working</h2>

<p>Main feature basically is a relay mechanism that relays important variables like location-cordinates, temperature, pressure, altitude, speed, etc from a drone to the nearest drones(vicinity can be choosen, preferably 2 kilometers). This creates an information sponge for the drone which can help drone absorb surrounding information and act accordingly. For now we have two basic features or modes of operations for the platform:</p>

<h3>Mono Mode</h3>

<p>In this mode drone is alone and receives information from surrounding drones and transmits its information to them. </p>

<h3>Fleet Mode</>

<p>In this mode drone is accompanied by fleetmates so that they can share their info no matter where they are to remain in contact and to aware of their fleetmates.</p>

<h2>Business Plan</h2>

<p>UAV's are damn inevitable. But still they are just at starting phase so we'll have to focus on drone pilots help and them use their drone out of the line-of-site. And because we'll be the very-early-mover, we'll have the advantage. </p>

<p> We can charge them on the volume of data received. That'll be our basic revenue model</p>

<h2>Technicals</h2>

<p>We used websockets to seamlessly transmit data between drones(which for now is our browsers and a poorly-coded python bot we craeted). We used Django as web-framework and Django Channels to make websockets work. At the front side we used Vue-Js.<p>

<h2>In Team:</h2>
<ul>
    <li>Saurav Niraula</li>
    <li>Sudesh Mate</li>
    <li>Suraj Bhattarai</li>
    <li>Suraj Jha</li>
</ul>


<h3> References </h3>

<ul>
    <li><a href = "https://www.djangoproject.com/">Django</a></li>
    <li><a href = "https://channels.readthedocs.io/en/latest/"> Django Channels </a></li>
    <li><a href = "https://vuejs.org/">Vue JS </a></li>
    <li><a href = "https://pypi.org/project/channels-redis/">Channels Redis</a></li>
    <li><a href  = "https://pypi.org/project/websocket_client/"> Python Websocket Client</a></li>