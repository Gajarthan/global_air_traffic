# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--11_20:11:09_UTC-green)

![Flight Map](images/flight_map.png)

## About

Historical archive of saved air traffic routes collected from the [OpenSky Network](https://opensky-network.org/) API. This repository keeps appending completed flights to `data/flights/` and rebuilds the visuals from the full archive.

**Data Source:** Saved route files in `data/flights/` (originally fetched from OpenSky `/flights/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches recently completed routes from OpenSky
- Saves each route as a JSON file in `data/flights/`
- Rebuilds aggregate statistics from all saved historical routes
- Generates a historical route map and archive summary
- Generates daily reports, weekly leaderboards, and timelapse GIFs

## Route Timelapse

![Timelapse](images/timelapse.gif)

## Archive Snapshot

**Latest saved flight:** 2026-07-11 20:11:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-11 20:11:09 UTC

- **137,992** saved flights
- **46,546** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **137,992** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,657,280.0 tonnes** estimated CO2 emissions
- **96,074,203 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5611 |
| 2 | SkyWest Airlines | 5066 |
| 3 | EJA | 2712 |
| 4 | IndiGo | 2535 |
| 5 | American Airlines | 2171 |
| 6 | Southwest Airlines | 2083 |
| 7 | ENY | 1731 |
| 8 | Delta Air Lines | 1638 |
| 9 | Lufthansa | 1409 |
| 10 | LATAM Airlines | 1269 |
| 11 | Vueling | 1193 |
| 12 | WIF | 1190 |
| 13 | AZU | 1187 |
| 14 | LXJ | 1060 |
| 15 | AXM | 1032 |
| 16 | Swiss International | 983 |
| 17 | easyJet | 894 |
| 18 | All Nippon Airways | 890 |
| 19 | Alaska Airlines | 870 |
| 20 | QLK | 856 |
| 21 | EJU | 847 |
| 22 | VIV | 756 |
| 23 | AEE | 747 |
| 24 | CXK | 739 |
| 25 | Air France | 738 |
| 26 | United Airlines | 727 |
| 27 | Cathay Pacific | 726 |
| 28 | JetBlue | 724 |
| 29 | MXY | 719 |
| 30 | GLO | 708 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 118578 |
| 2 | 🇪🇸 ES | 9081 |
| 3 | 🇮🇳 IN | 7947 |
| 4 | 🇦🇺 AU | 7874 |
| 5 | 🇧🇷 BR | 7796 |
| 6 | 🇨🇦 CA | 7263 |
| 7 | 🇮🇹 IT | 7207 |
| 8 | 🇩🇪 DE | 7202 |
| 9 | 🇬🇧 GB | 6255 |
| 10 | 🇯🇵 JP | 5816 |
| 11 | 🇫🇷 FR | 5491 |
| 12 | 🇨🇴 CO | 4356 |
| 13 | 🇲🇽 MX | 4000 |
| 14 | 🇬🇷 GR | 3938 |
| 15 | 🇳🇴 NO | 3720 |
| 16 | 🇨🇭 CH | 3576 |
| 17 | 🇹🇷 TR | 3213 |
| 18 | 🇲🇾 MY | 2682 |
| 19 | 🇵🇱 PL | 2316 |
| 20 | 🇿🇦 ZA | 2260 |
| 21 | 🇳🇿 NZ | 2122 |
| 22 | 🇹🇭 TH | 2092 |
| 23 | 🇰🇷 KR | 1997 |
| 24 | 🇵🇭 PH | 1883 |
| 25 | 🇬🇹 GT | 1839 |
| 26 | 🇲🇦 MA | 1454 |
| 27 | 🇲🇪 ME | 1369 |
| 28 | 🇳🇱 NL | 1285 |
| 29 | 🇭🇷 HR | 1249 |
| 30 | 🇲🇴 MO | 1186 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2866 |
| 2 | Denver International Airport |  | US | 2312 |
| 3 | Tokyo International Airport |  | JP | 1897 |
| 4 | Indira Gandhi International Airport |  | IN | 1757 |
| 5 | Harry Reid International Airport |  | US | 1725 |
| 6 | Guaymaral Airport |  | CO | 1680 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1601 |
| 8 | Zurich Airport |  | CH | 1533 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1455 |
| 10 | La Aurora Airport |  | GT | 1421 |
| 11 | Frankfurt am Main International Airport |  | DE | 1364 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1323 |
| 13 | Chicago O'Hare International Airport |  | US | 1303 |
| 14 | El Dorado International Airport |  | CO | 1228 |
| 15 | Salt Lake City International Airport |  | US | 1225 |
| 16 | Macau International Airport |  | MO | 1186 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1184 |
| 18 | Capua Airport |  | IT | 1132 |
| 19 | Madrid Barajas International Airport |  | ES | 1123 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1113 |
| 21 | Congonhas Airport |  | BR | 1111 |
| 22 | Kuala Lumpur International Airport |  | MY | 1040 |
| 23 | Charlotte/Douglas International Airport |  | US | 1010 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 990 |
| 25 | Charles de Gaulle International Airport |  | FR | 982 |
| 26 | Bengaluru International Airport |  | IN | 955 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 953 |
| 28 | Malpensa International Airport |  | IT | 901 |
| 29 | Ninoy Aquino International Airport |  | PH | 876 |
| 30 | Daniel K Inouye International Airport |  | US | 848 |
| 31 | Barcelona International Airport |  | ES | 840 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 839 |
| 33 | Tenerife Norte Airport |  | ES | 812 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 809 |
| 35 | Calgary International Airport |  | CA | 800 |
| 36 | Viracopos International Airport |  | BR | 791 |
| 37 | Scottsdale Airport |  | US | 790 |
| 38 | Seattle-Tacoma International Airport |  | US | 785 |
| 39 | Vitoria/Foronda Airport |  | ES | 775 |
| 40 | Amsterdam Airport Schiphol |  | NL | 770 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 707 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 498 | 21m | 244 km | 2,096.9 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 340 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 338 | 24m | 225 km | 1,311.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 330 | 1h 9m | 770 km | 4,383.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 296 | 14m | 114 km | 580.6 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 258 | 26m | 275 km | 1,222.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 251 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 205 | 22m | 55 km | 194.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 189 | 26m | 215 km | 700.0 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 189 | 44m | 241 km | 785.1 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 186 | 1h 46m | 1,423 km | 4,564.7 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 185 | 20m | 99 km | 316.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 182 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 176 | 27m | 152 km | 460.0 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 171 | 20m | 250 km | 738.6 t |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 169 | 31m | 369 km | 1,075.7 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 166 | 18m | 144 km | 412.9 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 163 | 44m | 452 km | 1,270.3 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 160 | 1h 16m | 961 km | 2,652.1 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 159 | 1h 1m | 695 km | 1,905.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 156 | 1h 38m | 1,156 km | 3,112.1 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 150 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N87JF |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-07-11 19:23 UTC | 2026-07-11 20:11 UTC | 47m |
| HLE65 | HLE | Badminton Airfield (EG03) | Cardiff International Airport (EGFF) | 2026-07-11 19:47 UTC | 2026-07-11 20:07 UTC | 19m |
| ERU851 | ERU | Ormond Beach Municipal Airport (KOMN) | Daytona Beach International Airport (KDAB) | 2026-07-11 19:40 UTC | 2026-07-11 20:04 UTC | 23m |
| N922ST |  | Wallom Field (8CA8) | Truckee-Tahoe Airport (KTRK) | 2026-07-11 19:29 UTC | 2026-07-11 20:01 UTC | 31m |
| N1361M |  | San Carlos Airport (KSQL) | San Carlos Airport (KSQL) | 2026-07-11 19:20 UTC | 2026-07-11 20:00 UTC | 39m |
| N775TH |  | Ralph Wien Memorial Airport (PAOT) | Ambler Airport (PAFM) | 2026-07-11 18:53 UTC | 2026-07-11 19:58 UTC | 1h 4m |
| ERU861 | ERU | Ormond Beach Municipal Airport (KOMN) | Cross Creek Farms Airport (04FL) | 2026-07-11 19:51 UTC | 2026-07-11 19:56 UTC | 4m |
| CXK203 | CXK | Hayward Executive Airport (KHWD) | Modesto City-County-Harry Sham Field (KMOD) | 2026-07-11 18:27 UTC | 2026-07-11 19:55 UTC | 1h 27m |
| N886TW |  | Watsonville Municipal Airport (KWVI) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-07-11 19:39 UTC | 2026-07-11 19:55 UTC | 15m |
| N680EA |  | Birmingham-Shuttlesworth International Airport (KBHM) | MI24 (MI24) | 2026-07-11 18:16 UTC | 2026-07-11 19:53 UTC | 1h 36m |
| N540AW |  | Palo Alto Airport (KPAO) | Las Trancas Airport (17CL) | 2026-07-11 19:40 UTC | 2026-07-11 19:52 UTC | 12m |
| CAP1074 | CAP | KS67 (KS67) | Hidden Lakes Airport (ID44) | 2026-07-11 19:29 UTC | 2026-07-11 19:51 UTC | 21m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-07-11 19:34 UTC | 2026-07-11 19:51 UTC | 16m |
| N605NC |  | Fremont County Airport (K1V6) | 14CO (14CO) | 2026-07-11 19:13 UTC | 2026-07-11 19:47 UTC | 33m |
| N9055F |  | Ralph Wien Memorial Airport (PAOT) | Ambler Airport (PAFM) | 2026-07-11 18:55 UTC | 2026-07-11 19:46 UTC | 51m |
| N951S |  | Washington County Airport (KAFJ) | Geary A Bates/Jefferson County Airpark (K2G2) | 2026-07-11 19:20 UTC | 2026-07-11 19:45 UTC | 24m |
| N4841Y |  | Kelly Air Park (CO15) | Kelly Air Park (CO15) | 2026-07-11 19:26 UTC | 2026-07-11 19:44 UTC | 17m |
| HK4350 |  | Alfredo Vasquez Cobo International Airport (SKLT) | Ipiranga Airport (SWII) | 2026-07-11 19:21 UTC | 2026-07-11 19:42 UTC | 20m |
| PDT888Q | PDT | Québec City Jean Lesage International Airport (CYQB) | Philadelphia International Airport (KPHL) | 2026-07-11 17:51 UTC | 2026-07-11 19:42 UTC | 1h 51m |
| N232ST |  | Truckee-Tahoe Airport (KTRK) | Palo Alto Airport (KPAO) | 2026-07-11 19:01 UTC | 2026-07-11 19:41 UTC | 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
