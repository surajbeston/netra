<h1> Aerial Netra </h2>

<h2>Introduction:</h2>

<img src="https://i.ibb.co/2dzV1GM/netra.png" alt="netra" border="0">

<p>Aerial Netra is a web platform that help drones transfer and receive data for higher security and better descision making. Basically aerial flight specially UASs or UAVs are much prone to accidents, very much due to unhealthy cloud conditions imprecise, detecting sensors and a lots of other reasons. And a lot of these happenings can simply be solved by transmitting surrounding data to them. And that's our solution, to suppy aerial vehicles with surrounding info from similar aerial vehicles around them. This can also help drone pilots to be aware od their drone's situation and surrounding to make descisions about the flight. </p>

<h2>Basic Working:</h2>

<p>Main feature basically is a relay mechanism that relays important variables like location-cordinates, temperature, pressure, altitude, speed, etc from a drone to nearest drones(vicinity can be choosen, for now 3 kilometers). This creates an information sponge for the drone which can help drone absorb surrounding information and act accordingly. For now we have two basic features or modes of operations for the platform:</p>

<h3>Mono Mode</h3>

<p>In this mode drone is alone and receives information from surrounding drones and transmits its information to them. </p>

<h3>Fleet M<p>Main feature basically is a relay mechanism that relays important variables like location-cordinates, temperature, pressure, altitude, speed, etc from a drone to nearest drones(vicinity can be choosen, for now 3 kilometers). This creates an information sponge for the drone which can help drone absorb surrounding information and act accordingly. For now we have two basic features or modes of operations for the platform:</p>

ode</h3>

<p>In this mode drone is accompanied by fleetmates so that they can share their info no matter where they are, to remain in contact and to aware of their fleetmates.</p>


<h2>Technicals:</h2>

<p>We used websockets to seamlessly transmit data between drones(which for now is our browsers and a poorly-coded python bot we created). We used Django as web-framework and Django Channels to make websockets work. For the front side, we used Vue-Js.<p>


<h2>Story:<h2>

<h3>Prologue</h2>
<p>We were thinking to do something with AR/VR with echoAR but then a short discussion on video chat drifted the idea to drones and then to our solution. We spent almost a couple of hours on topic research and planning and another hour on technical research jotting down packages.</p>

<h3>Characters</h3>
<p>Suraj Bhattarai started plucking out every piece we talked about and started defending his ideas. Saurav Niraula stayed quite in the ideation, only to start working like an ox afterwards. Sudesh Mate pointed out details and brought up technical spokes to support the project and Suraj Jha started connecting pieces to make them work.</p>

<h3>Challenges & solutions</h3>
<p>We didn't had hardware to do stuffs in the real way. So, we simulated browser as the drone and worked on it. Actually, noone had worked on websockets before and it was real pain understanding channels and groups and making them work through a series of "console.log"s. </p>

<h3>In the nutshell</h3>
<p>We started rapidly at first but then slowed in the middle due to issues with websockets and mapbox integration(mapbox was really and is), then again things went well and we satisfactorily pulled out our project.</p>

<h2>Business Plan:</h2>

<p>UAV's are damn inevitable. But still they are just at starting phase so we'll have to focus on drone pilots help and them use their drone out of the line-of-site. And because we'll be the very-early-mover, we'll have the advantage. </p>

<p> We can charge them on the volume of data received. That'll be our basic revenue model</p>


<h2>In Team:</h2>
<ul>
    <li><b>Saurav Niraula<b> Worked in frontend. Integrated MapBox and worked with Vue Js.</li>
    <li><b>Sudesh Mate<b> Helped in research and worked on drone navigation.</li>
    <li><b>Suraj Bhattarai<b> Worked on idea, design and documented the entire thing. </li>
    <li><b>Suraj Jha<b> Created backend and helped to integrate it with Vue.</li>
</ul>


<h3> References: </h3>

<ul>
    <li><a href = "https://www.djangoproject.com/">Django</a></li>
    <li><a href = "https://channels.readthedocs.io/en/latest/"> Django Channels </a></li>
    <li><a href = "https://vuejs.org/">Vue JS </a></li>
    <li><a href = "https://pypi.org/project/channels-redis/">Channels Redis</a></li>
    <li><a href  = "https://pypi.org/project/websocket_client/"> Python Websocket Client</a></li>
    <li><a href = "https://docs.mapbox.com/mapbox-gl-js/api/"> Mapbox </a></li>
