# AppleStoreSupervisor

> This Python script helps you supervise the availability of Apple products in Apple Stores.

All you need to do is enter the following lines in terminal and wish good luck with yourself.

```
git clone https://github.com/wangzhihao1995/AppleStoreSupervisor.git
cd AppleStoreSupervisor
python check_availability.py
```

If the target product is available, it will automatically launch your default browser and direct to the order page thanks to *webbrowser*.

Temporarily, this script only support supervising the availability of iPhone 7 Plus Black 128GB Version in Beijing's Apple Stores.
Don't worry, more powerful functions will be implemented before long.

## Updates
- 2016.09.28
    + Show update time when Apple Store is not available
- 2016.09.27
    + Would not crash if the network is down
- 2016.09.26
    + Show message if Apple Store is not available
    + Automatically refresh the availability with random interval
	+ Automatically launch default browser once the target is available and then direct to the order page instantly
    + Shutdown the program after directing to the order page
- 2016.09.25
	+ Check the availability of targert iPhone 7 Plus mannually
