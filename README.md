# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--11_13:52:32_UTC-green)

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

**Latest saved flight:** 2026-07-11 13:52:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-11 13:52:32 UTC

- **136,959** saved flights
- **46,220** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **136,959** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,646,056.2 tonnes** estimated CO2 emissions
- **95,423,550 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5565 |
| 2 | SkyWest Airlines | 5014 |
| 3 | EJA | 2680 |
| 4 | IndiGo | 2529 |
| 5 | American Airlines | 2150 |
| 6 | Southwest Airlines | 2063 |
| 7 | ENY | 1715 |
| 8 | Delta Air Lines | 1629 |
| 9 | Lufthansa | 1403 |
| 10 | LATAM Airlines | 1257 |
| 11 | WIF | 1190 |
| 12 | Vueling | 1189 |
| 13 | AZU | 1175 |
| 14 | LXJ | 1051 |
| 15 | AXM | 1032 |
| 16 | Swiss International | 980 |
| 17 | All Nippon Airways | 890 |
| 18 | easyJet | 888 |
| 19 | Alaska Airlines | 864 |
| 20 | QLK | 856 |
| 21 | EJU | 841 |
| 22 | VIV | 749 |
| 23 | AEE | 741 |
| 24 | Air France | 733 |
| 25 | CXK | 731 |
| 26 | Cathay Pacific | 726 |
| 27 | JetBlue | 720 |
| 28 | United Airlines | 718 |
| 29 | MXY | 710 |
| 30 | GLO | 701 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 117460 |
| 2 | 🇪🇸 ES | 9028 |
| 3 | 🇮🇳 IN | 7933 |
| 4 | 🇦🇺 AU | 7873 |
| 5 | 🇧🇷 BR | 7725 |
| 6 | 🇨🇦 CA | 7219 |
| 7 | 🇩🇪 DE | 7156 |
| 8 | 🇮🇹 IT | 7142 |
| 9 | 🇬🇧 GB | 6217 |
| 10 | 🇯🇵 JP | 5816 |
| 11 | 🇫🇷 FR | 5448 |
| 12 | 🇨🇴 CO | 4302 |
| 13 | 🇲🇽 MX | 3969 |
| 14 | 🇬🇷 GR | 3902 |
| 15 | 🇳🇴 NO | 3714 |
| 16 | 🇨🇭 CH | 3564 |
| 17 | 🇹🇷 TR | 3178 |
| 18 | 🇲🇾 MY | 2682 |
| 19 | 🇵🇱 PL | 2275 |
| 20 | 🇿🇦 ZA | 2256 |
| 21 | 🇳🇿 NZ | 2121 |
| 22 | 🇹🇭 TH | 2090 |
| 23 | 🇰🇷 KR | 1996 |
| 24 | 🇵🇭 PH | 1883 |
| 25 | 🇬🇹 GT | 1836 |
| 26 | 🇲🇦 MA | 1437 |
| 27 | 🇲🇪 ME | 1361 |
| 28 | 🇳🇱 NL | 1276 |
| 29 | 🇭🇷 HR | 1237 |
| 30 | 🇲🇴 MO | 1186 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2844 |
| 2 | Denver International Airport |  | US | 2290 |
| 3 | Tokyo International Airport |  | JP | 1897 |
| 4 | Indira Gandhi International Airport |  | IN | 1753 |
| 5 | Harry Reid International Airport |  | US | 1713 |
| 6 | Guaymaral Airport |  | CO | 1659 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1594 |
| 8 | Zurich Airport |  | CH | 1528 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1446 |
| 10 | La Aurora Airport |  | GT | 1418 |
| 11 | Frankfurt am Main International Airport |  | DE | 1359 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1312 |
| 13 | Chicago O'Hare International Airport |  | US | 1293 |
| 14 | El Dorado International Airport |  | CO | 1217 |
| 15 | Salt Lake City International Airport |  | US | 1212 |
| 16 | Macau International Airport |  | MO | 1186 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1180 |
| 18 | Madrid Barajas International Airport |  | ES | 1113 |
| 19 | Capua Airport |  | IT | 1113 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1108 |
| 21 | Congonhas Airport |  | BR | 1099 |
| 22 | Kuala Lumpur International Airport |  | MY | 1040 |
| 23 | Charlotte/Douglas International Airport |  | US | 1000 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 990 |
| 25 | Charles de Gaulle International Airport |  | FR | 977 |
| 26 | Bengaluru International Airport |  | IN | 952 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 945 |
| 28 | Malpensa International Airport |  | IT | 897 |
| 29 | Ninoy Aquino International Airport |  | PH | 876 |
| 30 | Daniel K Inouye International Airport |  | US | 843 |
| 31 | Barcelona International Airport |  | ES | 836 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 834 |
| 33 | Tenerife Norte Airport |  | ES | 812 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 806 |
| 35 | Calgary International Airport |  | CA | 797 |
| 36 | Scottsdale Airport |  | US | 784 |
| 37 | Viracopos International Airport |  | BR | 783 |
| 38 | Seattle-Tacoma International Airport |  | US | 781 |
| 39 | Vitoria/Foronda Airport |  | ES | 770 |
| 40 | Amsterdam Airport Schiphol |  | NL | 765 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 698 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 494 | 21m | 244 km | 2,080.1 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 339 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 338 | 24m | 225 km | 1,311.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 330 | 1h 9m | 770 km | 4,383.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 293 | 14m | 114 km | 574.7 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 255 | 26m | 275 km | 1,208.3 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 250 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 201 | 22m | 55 km | 191.0 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 189 | 26m | 215 km | 700.0 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 189 | 44m | 241 km | 785.1 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 185 | 1h 46m | 1,423 km | 4,540.2 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 185 | 20m | 99 km | 316.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 182 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 176 | 27m | 152 km | 460.0 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 170 | 20m | 250 km | 734.3 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 169 | 31m | 369 km | 1,075.7 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 165 | 18m | 144 km | 410.4 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 164 | 30m | 49 km | 138.6 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 163 | 44m | 452 km | 1,270.3 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 159 | 1h 16m | 961 km | 2,635.5 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 158 | 1h 1m | 695 km | 1,893.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 156 | 1h 38m | 1,156 km | 3,112.1 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 149 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N9131H |  | Manassas Regional/Harry P Davis Field (KHEF) | Culpeper Regional Airport (KCJR) | 2026-07-11 13:14 UTC | 2026-07-11 13:52 UTC | 37m |
| TJD650 | TJD | Torino / Caselle International Airport (LIMF) | Olbia / Costa Smeralda Airport (LIEO) | 2026-07-11 13:05 UTC | 2026-07-11 13:51 UTC | 46m |
| N13AK |  | Monmouth Executive Airport (KBLM) | NJ69 (NJ69) | 2026-07-11 13:20 UTC | 2026-07-11 13:50 UTC | 29m |
| N1240M |  | Bangor International Airport (KBGR) | Dewitt Field/Old Town Municipal Airport (KOLD) | 2026-07-11 13:26 UTC | 2026-07-11 13:49 UTC | 22m |
| 5903V |  | Illinois Valley Regional-Walter A Duncan Field (KVYS) | Illinois Valley Regional-Walter A Duncan Field (KVYS) | 2026-07-11 13:43 UTC | 2026-07-11 13:43 UTC | 0m |
| N422JC |  | 7MD0 (7MD0) | Wright Field (MD11) | 2026-07-11 12:45 UTC | 2026-07-11 13:42 UTC | 56m |
| 6VCEV |  | Friedrichshafen Airport (EDNY) | Marl Loemuhle Airport (EDLM) | 2026-07-11 12:42 UTC | 2026-07-11 13:38 UTC | 56m |
| DFFUN | DFF | Girona Airport (LEGE) | Stadtlohn-Vreden Airport (EDLS) | 2026-07-11 10:58 UTC | 2026-07-11 13:38 UTC | 2h 40m |
| DFKJM | DFK | London Biggin Hill Airport (EGKB) | Jena-Schongleina Airport (EDBJ) | 2026-07-11 11:33 UTC | 2026-07-11 13:38 UTC | 2h 5m |
| EWG53G | EWG | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Essen Mulheim Airport (EDLE) | 2026-07-11 12:15 UTC | 2026-07-11 13:38 UTC | 1h 22m |
| N562X |  | Ashland Landing Farm Airport (MD21) | Ashland Landing Farm Airport (MD21) | 2026-07-11 12:52 UTC | 2026-07-11 13:35 UTC | 43m |
| EXS89GV | EXS | Alicante International Airport (LEAL) | Manchester Airport (EGCC) | 2026-07-11 11:03 UTC | 2026-07-11 13:34 UTC | 2h 30m |
| BLVG | BLV | Chek Lap Kok International Airport (VHHH) | Chek Lap Kok International Airport (VHHH) | 2026-07-11 13:27 UTC | 2026-07-11 13:30 UTC | 2m |
| TVS1FG | TVS | Václav Havel Airport (LKPR) | Olbia / Costa Smeralda Airport (LIEO) | 2026-07-11 11:49 UTC | 2026-07-11 13:26 UTC | 1h 36m |
| N73KG |  | Phoenix Deer Valley Airport (KDVT) | 2AZ7 (2AZ7) | 2026-07-11 13:16 UTC | 2026-07-11 13:20 UTC | 3m |
| N1556 |  | Springfield-Branson Ntl Airport (KSGF) | Cantrell Farms Airport (AR06) | 2026-07-11 12:55 UTC | 2026-07-11 13:16 UTC | 21m |
| N576SC |  | Georgetown-Scott County Regional Airport (K27K) | Marion County Airport (KMAO) | 2026-07-11 12:17 UTC | 2026-07-11 13:15 UTC | 57m |
| JBU1160 | JetBlue | Philadelphia International Airport (KPHL) | Philadelphia International Airport (KPHL) | 2026-07-11 12:59 UTC | 2026-07-11 13:14 UTC | 15m |
| DHEMY | DHE | Saulgau Airport (EDTU) | Mengen-Hohentengen Airport (EDTM) | 2026-07-11 12:39 UTC | 2026-07-11 13:13 UTC | 33m |
| N672CA |  | UT99 (UT99) | Nephi Municipal Airport (KU14) | 2026-07-11 12:54 UTC | 2026-07-11 13:13 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
