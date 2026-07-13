# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--13_11:07:48_UTC-green)

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

**Latest saved flight:** 2026-07-13 11:07:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-13 11:07:48 UTC

- **139,892** saved flights
- **47,102** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **139,892** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,680,274.9 tonnes** estimated CO2 emissions
- **97,407,241 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5701 |
| 2 | SkyWest Airlines | 5120 |
| 3 | EJA | 2755 |
| 4 | IndiGo | 2570 |
| 5 | American Airlines | 2214 |
| 6 | Southwest Airlines | 2104 |
| 7 | ENY | 1743 |
| 8 | Delta Air Lines | 1656 |
| 9 | Lufthansa | 1425 |
| 10 | LATAM Airlines | 1284 |
| 11 | Vueling | 1210 |
| 12 | WIF | 1205 |
| 13 | AZU | 1203 |
| 14 | LXJ | 1072 |
| 15 | AXM | 1048 |
| 16 | Swiss International | 999 |
| 17 | easyJet | 913 |
| 18 | All Nippon Airways | 899 |
| 19 | Alaska Airlines | 881 |
| 20 | QLK | 877 |
| 21 | EJU | 863 |
| 22 | VIV | 772 |
| 23 | AEE | 752 |
| 24 | Air France | 752 |
| 25 | CXK | 750 |
| 26 | JetBlue | 735 |
| 27 | United Airlines | 731 |
| 28 | Cathay Pacific | 729 |
| 29 | MXY | 726 |
| 30 | GLO | 715 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 120079 |
| 2 | 🇪🇸 ES | 9190 |
| 3 | 🇮🇳 IN | 8053 |
| 4 | 🇦🇺 AU | 8016 |
| 5 | 🇧🇷 BR | 7888 |
| 6 | 🇨🇦 CA | 7330 |
| 7 | 🇮🇹 IT | 7313 |
| 8 | 🇩🇪 DE | 7308 |
| 9 | 🇬🇧 GB | 6374 |
| 10 | 🇯🇵 JP | 5895 |
| 11 | 🇫🇷 FR | 5579 |
| 12 | 🇨🇴 CO | 4421 |
| 13 | 🇲🇽 MX | 4057 |
| 14 | 🇬🇷 GR | 3985 |
| 15 | 🇳🇴 NO | 3770 |
| 16 | 🇨🇭 CH | 3640 |
| 17 | 🇹🇷 TR | 3291 |
| 18 | 🇲🇾 MY | 2731 |
| 19 | 🇵🇱 PL | 2342 |
| 20 | 🇿🇦 ZA | 2298 |
| 21 | 🇳🇿 NZ | 2142 |
| 22 | 🇹🇭 TH | 2109 |
| 23 | 🇰🇷 KR | 2013 |
| 24 | 🇵🇭 PH | 1906 |
| 25 | 🇬🇹 GT | 1848 |
| 26 | 🇲🇦 MA | 1468 |
| 27 | 🇲🇪 ME | 1391 |
| 28 | 🇳🇱 NL | 1318 |
| 29 | 🇭🇷 HR | 1264 |
| 30 | 🇲🇴 MO | 1190 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2887 |
| 2 | Denver International Airport |  | US | 2341 |
| 3 | Tokyo International Airport |  | JP | 1909 |
| 4 | Indira Gandhi International Airport |  | IN | 1783 |
| 5 | Harry Reid International Airport |  | US | 1746 |
| 6 | Guaymaral Airport |  | CO | 1701 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1612 |
| 8 | Zurich Airport |  | CH | 1560 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1466 |
| 10 | La Aurora Airport |  | GT | 1428 |
| 11 | Frankfurt am Main International Airport |  | DE | 1374 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1335 |
| 13 | Chicago O'Hare International Airport |  | US | 1316 |
| 14 | Salt Lake City International Airport |  | US | 1244 |
| 15 | El Dorado International Airport |  | CO | 1240 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1199 |
| 17 | Macau International Airport |  | MO | 1190 |
| 18 | Capua Airport |  | IT | 1147 |
| 19 | Madrid Barajas International Airport |  | ES | 1139 |
| 20 | Congonhas Airport |  | BR | 1122 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1120 |
| 22 | Kuala Lumpur International Airport |  | MY | 1057 |
| 23 | Charlotte/Douglas International Airport |  | US | 1022 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1011 |
| 25 | Charles de Gaulle International Airport |  | FR | 995 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 970 |
| 27 | Bengaluru International Airport |  | IN | 963 |
| 28 | Malpensa International Airport |  | IT | 910 |
| 29 | Ninoy Aquino International Airport |  | PH | 889 |
| 30 | Daniel K Inouye International Airport |  | US | 857 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 854 |
| 32 | Barcelona International Airport |  | ES | 854 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 821 |
| 34 | Tenerife Norte Airport |  | ES | 818 |
| 35 | Calgary International Airport |  | CA | 804 |
| 36 | Viracopos International Airport |  | BR | 798 |
| 37 | Seattle-Tacoma International Airport |  | US | 796 |
| 38 | Scottsdale Airport |  | US | 793 |
| 39 | Amsterdam Airport Schiphol |  | NL | 792 |
| 40 | Vitoria/Foronda Airport |  | ES | 780 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 717 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 507 | 21m | 244 km | 2,134.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 344 | 24m | 225 km | 1,334.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 342 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 333 | 1h 9m | 770 km | 4,423.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 298 | 14m | 114 km | 584.5 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 258 | 26m | 275 km | 1,222.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 254 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 206 | 22m | 55 km | 195.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 191 | 26m | 215 km | 707.4 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 190 | 44m | 241 km | 789.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 187 | 1h 46m | 1,423 km | 4,589.3 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 186 | 20m | 99 km | 318.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 185 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 176 | 27m | 152 km | 460.0 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 175 | 20m | 250 km | 755.9 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 170 | 31m | 369 km | 1,082.1 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 168 | 18m | 144 km | 417.9 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 164 | 44m | 452 km | 1,278.1 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 162 | 1h 16m | 961 km | 2,685.2 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 161 | 1h 1m | 695 km | 1,929.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 158 | 1h 38m | 1,156 km | 3,152.0 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 156 | 14m | 154 km | 413.3 t |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 154 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N292AM |  | K61B (K61B) | Harry Reid International Airport (KLAS) | 2026-07-13 10:56 UTC | 2026-07-13 11:07 UTC | 10m |
| AE974 |  | Tamworth Airport (YSTW) | Port Macquarie Airport (YPMQ) | 2026-07-13 10:35 UTC | 2026-07-13 11:00 UTC | 25m |
| N562X |  | Belfair Airport (DE32) | Belfair Airport (DE32) | 2026-07-13 10:48 UTC | 2026-07-13 10:57 UTC | 8m |
| DEVMV | DEV | Adolf Wurth Airport (EDTY) | Straubing Airport (EDMS) | 2026-07-13 09:44 UTC | 2026-07-13 10:55 UTC | 1h 11m |
| DMMLS | DMM | Meppe Airport (ETWM) | Meppe Airport (ETWM) | 2026-07-13 10:23 UTC | 2026-07-13 10:54 UTC | 30m |
| N818BT |  | Delaware Coastal Airport (KGED) | Ocean City Municipal Airport (KOXB) | 2026-07-13 10:43 UTC | 2026-07-13 10:54 UTC | 10m |
| AIC219 | Air India | Indira Gandhi International Airport (VIDP) | Simara Airport (VNSI) | 2026-07-13 09:14 UTC | 2026-07-13 10:45 UTC | 1h 31m |
| SHA736 | SHA | Langtang Airport (VNLT) | Langtang Airport (VNLT) | 2026-07-13 10:42 UTC | 2026-07-13 10:43 UTC | 1m |
| AAL437P | American Airlines | Harry Reid International Airport (KLAS) | Philadelphia International Airport (KPHL) | 2026-07-13 06:10 UTC | 2026-07-13 10:33 UTC | 4h 23m |
| UBA582 | UBA | Monywar Airport (VYMY) | Phonngbyin Airport (VYPB) | 2026-07-13 10:03 UTC | 2026-07-13 10:29 UTC | 26m |
| PLF106 | PLF | Hamburg Airport (EDDH) | Stuttgart Airport (EDDS) | 2026-07-13 09:28 UTC | 2026-07-13 10:23 UTC | 54m |
| SFR201 | SFR | Cape Town International Airport (FACT) | Tedderfield Air Park (FATA) | 2026-07-13 08:37 UTC | 2026-07-13 10:22 UTC | 1h 45m |
| YEL8 | YEL | Norman Y Mineta San Jose International Airport (KSJC) | Palm Springs International Airport (KPSP) | 2026-07-13 09:23 UTC | 2026-07-13 10:19 UTC | 55m |
| YHT | YHT | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-07-13 09:53 UTC | 2026-07-13 10:16 UTC | 23m |
| ANE83RZ | ANE | Palma De Mallorca Airport (LEPA) | Menorca Airport (LEMH) | 2026-07-13 09:44 UTC | 2026-07-13 10:16 UTC | 32m |
| VLG83CM | Vueling | Palma De Mallorca Airport (LEPA) | Bilbao Airport (LEBB) | 2026-07-13 09:22 UTC | 2026-07-13 10:16 UTC | 54m |
| SAS1320 | Scandinavian Airlines | Oslo Gardermoen Airport (ENGM) | Ørsta-Volda Airport Hovden (ENOV) | 2026-07-13 09:44 UTC | 2026-07-13 10:14 UTC | 30m |
| SHDW11 | SHD | RAAF Base Pearce (YPEA) | RAAF Gingin (YGIG) | 2026-07-13 09:59 UTC | 2026-07-13 10:14 UTC | 14m |
| FIN5P | Finnair | Bergen Airport Flesland (ENBR) | Stockholm-Arlanda Airport (ESSA) | 2026-07-13 09:06 UTC | 2026-07-13 10:13 UTC | 1h 7m |
| OC61 |  | Nagasaki Airport (RJFU) | Iki Airport (RJDB) | 2026-07-13 10:03 UTC | 2026-07-13 10:13 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
