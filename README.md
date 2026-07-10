# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--10_11:11:20_UTC-green)

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

**Latest saved flight:** 2026-07-10 11:11:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-10 11:11:20 UTC

- **135,460** saved flights
- **45,787** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **135,460** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,630,461.9 tonnes** estimated CO2 emissions
- **94,519,532 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5492 |
| 2 | SkyWest Airlines | 4984 |
| 3 | EJA | 2646 |
| 4 | IndiGo | 2507 |
| 5 | American Airlines | 2133 |
| 6 | Southwest Airlines | 2038 |
| 7 | ENY | 1703 |
| 8 | Delta Air Lines | 1617 |
| 9 | Lufthansa | 1391 |
| 10 | LATAM Airlines | 1242 |
| 11 | Vueling | 1181 |
| 12 | WIF | 1178 |
| 13 | AZU | 1163 |
| 14 | LXJ | 1040 |
| 15 | AXM | 1028 |
| 16 | Swiss International | 964 |
| 17 | All Nippon Airways | 882 |
| 18 | easyJet | 877 |
| 19 | Alaska Airlines | 860 |
| 20 | QLK | 851 |
| 21 | EJU | 833 |
| 22 | VIV | 745 |
| 23 | AEE | 734 |
| 24 | CXK | 728 |
| 25 | Cathay Pacific | 725 |
| 26 | Air France | 724 |
| 27 | JetBlue | 715 |
| 28 | United Airlines | 715 |
| 29 | MXY | 705 |
| 30 | GLO | 690 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 116263 |
| 2 | 🇪🇸 ES | 8958 |
| 3 | 🇮🇳 IN | 7868 |
| 4 | 🇦🇺 AU | 7826 |
| 5 | 🇧🇷 BR | 7637 |
| 6 | 🇨🇦 CA | 7162 |
| 7 | 🇩🇪 DE | 7055 |
| 8 | 🇮🇹 IT | 7019 |
| 9 | 🇬🇧 GB | 6110 |
| 10 | 🇯🇵 JP | 5770 |
| 11 | 🇫🇷 FR | 5373 |
| 12 | 🇨🇴 CO | 4247 |
| 13 | 🇲🇽 MX | 3941 |
| 14 | 🇬🇷 GR | 3855 |
| 15 | 🇳🇴 NO | 3672 |
| 16 | 🇨🇭 CH | 3504 |
| 17 | 🇹🇷 TR | 3095 |
| 18 | 🇲🇾 MY | 2670 |
| 19 | 🇵🇱 PL | 2243 |
| 20 | 🇿🇦 ZA | 2229 |
| 21 | 🇳🇿 NZ | 2117 |
| 22 | 🇹🇭 TH | 2069 |
| 23 | 🇰🇷 KR | 1991 |
| 24 | 🇵🇭 PH | 1861 |
| 25 | 🇬🇹 GT | 1827 |
| 26 | 🇲🇦 MA | 1430 |
| 27 | 🇲🇪 ME | 1344 |
| 28 | 🇳🇱 NL | 1264 |
| 29 | 🇭🇷 HR | 1205 |
| 30 | 🇲🇴 MO | 1186 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2822 |
| 2 | Denver International Airport |  | US | 2279 |
| 3 | Tokyo International Airport |  | JP | 1884 |
| 4 | Indira Gandhi International Airport |  | IN | 1739 |
| 5 | Harry Reid International Airport |  | US | 1695 |
| 6 | Guaymaral Airport |  | CO | 1647 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1581 |
| 8 | Zurich Airport |  | CH | 1507 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1435 |
| 10 | La Aurora Airport |  | GT | 1412 |
| 11 | Frankfurt am Main International Airport |  | DE | 1346 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1304 |
| 13 | Chicago O'Hare International Airport |  | US | 1285 |
| 14 | Salt Lake City International Airport |  | US | 1208 |
| 15 | El Dorado International Airport |  | CO | 1206 |
| 16 | Macau International Airport |  | MO | 1186 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1176 |
| 18 | Madrid Barajas International Airport |  | ES | 1105 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1104 |
| 20 | Capua Airport |  | IT | 1103 |
| 21 | Congonhas Airport |  | BR | 1086 |
| 22 | Kuala Lumpur International Airport |  | MY | 1036 |
| 23 | Charlotte/Douglas International Airport |  | US | 995 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 985 |
| 25 | Charles de Gaulle International Airport |  | FR | 967 |
| 26 | Bengaluru International Airport |  | IN | 946 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 930 |
| 28 | Malpensa International Airport |  | IT | 890 |
| 29 | Ninoy Aquino International Airport |  | PH | 866 |
| 30 | Daniel K Inouye International Airport |  | US | 839 |
| 31 | Barcelona International Airport |  | ES | 831 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 829 |
| 33 | Tenerife Norte Airport |  | ES | 807 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 795 |
| 35 | Calgary International Airport |  | CA | 786 |
| 36 | Seattle-Tacoma International Airport |  | US | 774 |
| 37 | Scottsdale Airport |  | US | 773 |
| 38 | Viracopos International Airport |  | BR | 772 |
| 39 | Vitoria/Foronda Airport |  | ES | 763 |
| 40 | Amsterdam Airport Schiphol |  | NL | 758 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 693 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 490 | 21m | 244 km | 2,063.3 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 338 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 334 | 24m | 225 km | 1,295.8 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 325 | 1h 10m | 770 km | 4,317.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 289 | 14m | 114 km | 566.8 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 252 | 26m | 275 km | 1,194.1 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 245 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 198 | 22m | 55 km | 188.2 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 188 | 26m | 215 km | 696.3 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 188 | 44m | 241 km | 780.9 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 185 | 20m | 99 km | 316.9 t |
| 17 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 183 | 1h 46m | 1,423 km | 4,491.1 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 180 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 175 | 27m | 152 km | 457.3 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 166 | 31m | 369 km | 1,056.6 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 165 | 20m | 250 km | 712.7 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 163 | 18m | 144 km | 405.5 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 162 | 30m | 49 km | 136.9 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 161 | 44m | 452 km | 1,254.8 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 159 | 1h 16m | 961 km | 2,635.5 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 157 | 1h 1m | 695 km | 1,882.0 t |
| 27 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 155 | 1h 38m | 1,156 km | 3,092.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 149 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SFY3DB | SFY | Bournemouth Airport (EGHH) | Exeter International Airport (EGTE) | 2026-07-10 10:36 UTC | 2026-07-10 11:11 UTC | 34m |
| GCMLY | GCM | Henstridge Airfield (EGHS) | Henstridge Airfield (EGHS) | 2026-07-10 09:55 UTC | 2026-07-10 11:02 UTC | 1h 7m |
| AVA254 | Avianca | El Dorado International Airport (SKBO) | Toronto Pearson International Airport (CYYZ) | 2026-07-10 05:29 UTC | 2026-07-10 11:00 UTC | 5h 31m |
| ERU811 | ERU | Daytona Beach International Airport (KDAB) | Skinners Wholesale Nursery Airport (16FD) | 2026-07-10 10:08 UTC | 2026-07-10 10:59 UTC | 50m |
| N24108 |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-07-10 10:36 UTC | 2026-07-10 10:55 UTC | 19m |
| BBC373 | BBC | VGZR (VGZR) | Tribhuvan International Airport (VNKT) | 2026-07-10 09:57 UTC | 2026-07-10 10:51 UTC | 53m |
| LIFELN4 | LIF | Eelde Airport (EHGG) | Hoogeveen Airport (EHHO) | 2026-07-10 10:34 UTC | 2026-07-10 10:50 UTC | 16m |
| N240GS |  | Old Sarum Airfield (EGLS) | Old Sarum Airfield (EGLS) | 2026-07-10 10:32 UTC | 2026-07-10 10:43 UTC | 10m |
| LRQ294D | LRQ | Eleftherios Venizelos International Airport (LGAV) | LW72 (LW72) | 2026-07-10 09:59 UTC | 2026-07-10 10:38 UTC | 39m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-07-10 10:12 UTC | 2026-07-10 10:37 UTC | 24m |
| SAXON17 | SAX | Earls Colne Airfield (EGSR) | London City Airport (EGLC) | 2026-07-10 10:15 UTC | 2026-07-10 10:36 UTC | 20m |
| 7TWJC |  | El Bayadh Airport (DAOY) | Bou Sfer Airport (DAOE) | 2026-07-10 09:51 UTC | 2026-07-10 10:32 UTC | 40m |
| RYR3RK | Ryanair | Berlin Brandenburg Airport (EDDB) | Manchester Airport (EGCC) | 2026-07-10 08:31 UTC | 2026-07-10 10:29 UTC | 1h 57m |
| HRN171 | HRN | Lubeck Blankensee Airport (EDHL) | Kiel-Holtenau Airport (EDHK) | 2026-07-10 10:14 UTC | 2026-07-10 10:28 UTC | 14m |
| RYR8V | Ryanair | Sandefjord Airport Torp (ENTO) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-07-10 08:53 UTC | 2026-07-10 10:27 UTC | 1h 34m |
| SWR4EA | Swiss International | Nice-Cote d'Azur Airport (LFMN) | Zurich Airport (LSZH) | 2026-07-10 09:08 UTC | 2026-07-10 10:26 UTC | 1h 17m |
| N1807T |  | New Garden Airport (KN57) | New Garden Airport (KN57) | 2026-07-10 10:08 UTC | 2026-07-10 10:25 UTC | 17m |
| SWR892M | Swiss International | Geneva Cointrin International Airport (LSGG) | Ibiza Airport (LEIB) | 2026-07-10 08:57 UTC | 2026-07-10 10:21 UTC | 1h 24m |
| AXM6484 | AXM | Kota Kinabalu International Airport (WBKK) | Telupid Airport (WBKE) | 2026-07-10 10:05 UTC | 2026-07-10 10:20 UTC | 14m |
| SPSDW | SPS | Krosno Airport (EPKR) | Krosno Airport (EPKR) | 2026-07-10 10:07 UTC | 2026-07-10 10:16 UTC | 9m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
