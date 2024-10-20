<h1>ESP32 and Raspberry Pi Relay Control with Timed Automation and Future Temperature-Based RGB Control</h1>

<h2>Project Overview</h2>
<p>
    This project uses both <strong>ESP32</strong> and <strong>Raspberry Pi</strong> to control relays based on time schedules. The relays can be used to power various devices like lights (5V LED, 220V RGB/bulb) and other electronic appliances. This setup automates the turning on and off of devices at specified times during the day, making it ideal for use cases like:
</p>
<ul>
    <li><strong>Temple lights (5V LED)</strong>: Automatically turns on in the morning and evening.</li>
    <li><strong>Study lights (220V bulb)</strong>: Automated control for specific study hours.</li>
</ul>

<h3>Current Features:</h3>
<ol>
    <li><strong>ESP32 and Raspberry Pi Control</strong>: GPIO-based relay control using either an ESP32 or Raspberry Pi.</li>
    <li><strong>Scheduled Automation</strong>:
        <ul>
            <li><strong>5V Temple LED</strong>: Turns on in the morning from 7:00 AM to 9:00 AM and again in the evening from 5:30 PM to 7:00 PM.</li>
            <li><strong>220V Study Bulb</strong>: Turns on from 6:00 PM to 8:45 PM and 9:15 PM to 10:15 PM.</li>
        </ul>
    </li>
    <li><strong>Modular Setup</strong>: Additional relays can be added, such as a 220V power switch for powering other devices.</li>
</ol>

<h2>Hardware Components</h2>
<ul>
    <li><strong>ESP32 Development Board</strong> or <strong>Raspberry Pi</strong> (choose based on preference)</li>
    <li><strong>5V Relay Module</strong> (for controlling low voltage devices)</li>
    <li><strong>220V Relay Module</strong> (for controlling high voltage devices like bulbs)</li>
    <li><strong>RGB Lights</strong> (220V RGB strip or bulb)</li>
    <li><strong>Temperature Sensor</strong> (for future RGB control based on temperature)
        <ul>
            <li>DHT11, DHT22, or any other compatible temperature sensor.</li>
        </ul>
    </li>
</ul>

<h2>How It Works</h2>
<p>
    The <strong>ESP32</strong> or <strong>Raspberry Pi</strong> is connected to relay modules via GPIO pins, controlling multiple devices. The relays are turned on or off based on pre-programmed schedules.
</p>

<h3>GPIO Pin Configuration</h3>
<ul>
    <li><strong>Relay 1 (5V LED)</strong>: GPIO 17</li>
    <li><strong>Relay 2 (220V RGB/Bulb)</strong>: GPIO 27</li>
    <li><strong>Relay 3 (220V Power)</strong>: Reserved for future use.</li>
</ul>

<h2>Software Setup</h2>

<h3>For ESP32 (MicroPython)</h3>
<ol>
    <li>Flash MicroPython firmware onto the ESP32 using <code>esptool.py</code> or <strong>Thonny IDE</strong>.</li>
    <li>Install required libraries:
        <ul>
            <li><code>machine</code>: For GPIO control.</li>
            <li><code>time</code>: For adding delays.</li>
            <li><code>datetime</code>: To manage and check current time for relay operations.</li>
        </ul>
    </li>
</ol>

<h3>For Raspberry Pi (Python)</h3>
<ol>
    <li>Install <code>gpiod</code> library for GPIO control:
        <ul>
            <li>Run <code>sudo apt install python3-libgpiod</code> to install the required library.</li>
        </ul>
    </li>
    <li>Follow the provided Python code to automate relay control based on time schedules.</li>
</ol>

<h2>Code</h2>
<p>
    Check out the <code>main.py</code> file for the code that handles relay control based on time. The code includes logic for:
</p>
<ul>
    <li>Defining GPIO pins for relays.</li>
    <li>Setting up relay control for multiple time periods.</li>
    <li>Turning relays on/off based on real-time clock.</li>
</ul>

<h2>Future Features</h2>
<ol>
    <li><strong>Temperature-Based RGB Color Change</strong>:
        <ul>
            <li>Add a temperature sensor (e.g., <strong>DHT11</strong> or <strong>DHT22</strong>) to monitor the ambient temperature.</li>
            <li>Adjust the color of the RGB lights based on the temperature reading:</li>
            <ul>
                <li><strong>Cooler temperatures</strong>: Show cooler colors (e.g., blue).</li>
                <li><strong>Warmer temperatures</strong>: Show warmer colors (e.g., red/orange).</li>
            </ul>
        </ul>
    </li>
    <li><strong>Additional Device Automation</strong>: Use the third relay to power on/off other devices, such as a fan or heater, based on the time or temperature.</li>
    <li><strong>Mobile Control</strong>: Integrate a mobile app or web interface to manually override relay control or adjust the automation schedule remotely.</li>
</ol>