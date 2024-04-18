<?php
system ("python /var/www/html/wake.py 192.168.0.255 FF:FF:FF:FF:FF:FF")
header ("Location:index.html")
?>