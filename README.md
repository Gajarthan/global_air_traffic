# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_09:27:22_UTC-green)

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

**Latest saved flight:** 2026-08-09 09:27:22 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-09 09:27:22 UTC

- **180,592** saved flights
- **57,781** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **180,592** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,170,659.8 tonnes** estimated CO2 emissions
- **125,835,349 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7149 |
| 2 | SkyWest Airlines | 6582 |
| 3 | EJA | 3555 |
| 4 | IndiGo | 3165 |
| 5 | Southwest Airlines | 2840 |
| 6 | American Airlines | 2817 |
| 7 | ENY | 2250 |
| 8 | Delta Air Lines | 2142 |
| 9 | LATAM Airlines | 1680 |
| 10 | AZU | 1613 |
| 11 | Lufthansa | 1605 |
| 12 | Vueling | 1494 |
| 13 | WIF | 1493 |
| 14 | LXJ | 1407 |
| 15 | easyJet | 1233 |
| 16 | Swiss International | 1229 |
| 17 | AXM | 1220 |
| 18 | QLK | 1115 |
| 19 | EJU | 1104 |
| 20 | All Nippon Airways | 1099 |
| 21 | Alaska Airlines | 1097 |
| 22 | VIV | 996 |
| 23 | GLO | 965 |
| 24 | Cathay Pacific | 946 |
| 25 | CXK | 946 |
| 26 | AEE | 943 |
| 27 | United Airlines | 929 |
| 28 | Air France | 928 |
| 29 | MXY | 905 |
| 30 | PGT | 905 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 154729 |
| 2 | 🇪🇸 ES | 11605 |
| 3 | 🇧🇷 BR | 10345 |
| 4 | 🇦🇺 AU | 10187 |
| 5 | 🇮🇳 IN | 9922 |
| 6 | 🇨🇦 CA | 9852 |
| 7 | 🇮🇹 IT | 9328 |
| 8 | 🇩🇪 DE | 8926 |
| 9 | 🇬🇧 GB | 8328 |
| 10 | 🇯🇵 JP | 7317 |
| 11 | 🇫🇷 FR | 7181 |
| 12 | 🇨🇴 CO | 6707 |
| 13 | 🇬🇷 GR | 5280 |
| 14 | 🇲🇽 MX | 5164 |
| 15 | 🇨🇭 CH | 4809 |
| 16 | 🇳🇴 NO | 4646 |
| 17 | 🇹🇷 TR | 4620 |
| 18 | 🇲🇾 MY | 3185 |
| 19 | 🇵🇱 PL | 3021 |
| 20 | 🇿🇦 ZA | 2942 |
| 21 | 🇹🇭 TH | 2763 |
| 22 | 🇳🇿 NZ | 2608 |
| 23 | 🇵🇭 PH | 2394 |
| 24 | 🇬🇹 GT | 2294 |
| 25 | 🇰🇷 KR | 2257 |
| 26 | 🇲🇦 MA | 1820 |
| 27 | 🇭🇷 HR | 1796 |
| 28 | 🇲🇪 ME | 1640 |
| 29 | 🇳🇱 NL | 1619 |
| 30 | 🇲🇴 MO | 1513 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3732 |
| 2 | Denver International Airport |  | US | 2987 |
| 3 | Tokyo International Airport |  | JP | 2272 |
| 4 | Guaymaral Airport |  | CO | 2223 |
| 5 | Indira Gandhi International Airport |  | IN | 2214 |
| 6 | Harry Reid International Airport |  | US | 2127 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1944 |
| 8 | Zurich Airport |  | CH | 1918 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1878 |
| 10 | La Aurora Airport |  | GT | 1762 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1648 |
| 12 | Chicago O'Hare International Airport |  | US | 1626 |
| 13 | Salt Lake City International Airport |  | US | 1616 |
| 14 | El Dorado International Airport |  | CO | 1611 |
| 15 | Frankfurt am Main International Airport |  | DE | 1566 |
| 16 | Macau International Airport |  | MO | 1513 |
| 17 | Congonhas Airport |  | BR | 1500 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1437 |
| 19 | Madrid Barajas International Airport |  | ES | 1419 |
| 20 | Capua Airport |  | IT | 1414 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1351 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1285 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1270 |
| 24 | Malpensa International Airport |  | IT | 1246 |
| 25 | Charlotte/Douglas International Airport |  | US | 1224 |
| 26 | Charles de Gaulle International Airport |  | FR | 1220 |
| 27 | Kuala Lumpur International Airport |  | MY | 1198 |
| 28 | Bengaluru International Airport |  | IN | 1179 |
| 29 | Ninoy Aquino International Airport |  | PH | 1127 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1122 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1109 |
| 32 | Barcelona International Airport |  | ES | 1075 |
| 33 | Seattle-Tacoma International Airport |  | US | 1041 |
| 34 | Daniel K Inouye International Airport |  | US | 1040 |
| 35 | Viracopos International Airport |  | BR | 1036 |
| 36 | Reno/Tahoe International Airport |  | US | 1032 |
| 37 | Calgary International Airport |  | CA | 1030 |
| 38 | Oslo Gardermoen Airport |  | NO | 998 |
| 39 | Tenerife Norte Airport |  | ES | 985 |
| 40 | Amsterdam Airport Schiphol |  | NL | 975 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 918 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 669 | 21m | 244 km | 2,817.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 430 | 1h 8m | 770 km | 5,712.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 426 | 24m | 225 km | 1,652.7 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 417 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 303 | 27m | 275 km | 1,435.8 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 298 | 1h 7m | 706 km | 3,628.2 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 270 | 44m | 241 km | 1,121.5 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 253 | 1h 48m | 1,423 km | 6,209.0 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 241 | 8m | - | - |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 237 | 20m | 250 km | 1,023.7 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 228 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 227 | 26m | 215 km | 840.7 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 221 | 19m | 99 km | 378.6 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 219 | 31m | 49 km | 185.1 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 219 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 218 | 1h 15m | 961 km | 3,613.5 t |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 218 | 50m | 556 km | 2,089.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 216 | 19m | 144 km | 537.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 212 | 1h 38m | 1,156 km | 4,229.3 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 210 | 31m | 369 km | 1,336.7 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 207 | 24m | 218 km | 779.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 203 | 28m | 152 km | 530.5 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 197 | 1h 1m | 695 km | 2,361.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| A6FTK |  | Al Minhad Air Base (OMDM) | Al Maktoum International Airport (OMDW) | 2026-08-09 08:38 UTC | 2026-08-09 09:27 UTC | 49m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-09 08:59 UTC | 2026-08-09 09:09 UTC | 10m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-08-09 08:33 UTC | 2026-08-09 08:48 UTC | 14m |
| N106AN |  | Lashenden (Headcorn) Airfield (EGKH) | Lashenden (Headcorn) Airfield (EGKH) | 2026-08-09 08:27 UTC | 2026-08-09 08:47 UTC | 19m |
| IBX42 | IBX | Hiroshima Airport (RJOA) | Fukushima Airport (RJSF) | 2026-08-09 07:38 UTC | 2026-08-09 08:44 UTC | 1h 5m |
| AEE5C | AEE | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 2026-08-09 08:25 UTC | 2026-08-09 08:43 UTC | 18m |
| 3AMAC |  | Nice-Cote d'Azur Airport (LFMN) | Nice-Cote d'Azur Airport (LFMN) | 2026-08-09 08:34 UTC | 2026-08-09 08:41 UTC | 6m |
| DEGLW | DEG | Wurzburg-Schenkenturm Airport (EDFW) | Wurzburg-Schenkenturm Airport (EDFW) | 2026-08-09 08:10 UTC | 2026-08-09 08:41 UTC | 30m |
| PGT1863 | PGT | Ercan International Airport (LCEN) | Selcuk Efes Airport (LTFB) | 2026-08-09 07:47 UTC | 2026-08-09 08:40 UTC | 53m |
| RGA06 | RGA | Locarno Airport (LSZL) | Lodrino Air Base (LSML) | 2026-08-09 08:37 UTC | 2026-08-09 08:39 UTC | 1m |
| AFR71PP | Air France | Charles de Gaulle International Airport (LFPG) | Wroughton Airfield (EGDT) | 2026-08-09 07:48 UTC | 2026-08-09 08:37 UTC | 49m |
| ICE30R | ICE | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 2026-08-09 08:15 UTC | 2026-08-09 08:36 UTC | 20m |
| EDW89P | EDW | Cagliari / Elmas Airport (LIEE) | Zurich Airport (LSZH) | 2026-08-09 07:08 UTC | 2026-08-09 08:32 UTC | 1h 24m |
| FSF258Z | FSF | Geneva Cointrin International Airport (LSGG) | Ghisonaccia Alzitone Airport (LFKG) | 2026-08-09 07:13 UTC | 2026-08-09 08:30 UTC | 1h 16m |
| DFOXI | DFO | Pruszcz Gdański Airport (EPPR) | Pruszcz Gdański Airport (EPPR) | 2026-08-09 08:07 UTC | 2026-08-09 08:29 UTC | 21m |
| VPCJE | VPC | Nice-Cote d'Azur Airport (LFMN) | Nice-Cote d'Azur Airport (LFMN) | 2026-08-09 08:21 UTC | 2026-08-09 08:28 UTC | 6m |
| VLG5ZB | Vueling | Faro Airport (LPFR) | Vitoria/Foronda Airport (LEVT) | 2026-08-09 07:24 UTC | 2026-08-09 08:27 UTC | 1h 3m |
| WZZ9NL | Wizz Air | Dortmund Airport (EDLW) | Tuzla International Airport (LQTZ) | 2026-08-09 07:00 UTC | 2026-08-09 08:25 UTC | 1h 25m |
| AUR201 | AUR | Alderney Airport (EGJA) | Guernsey Airport (EGJB) | 2026-08-09 08:12 UTC | 2026-08-09 08:24 UTC | 12m |
| N886LF |  | Boise Air Trml/Gowen Field (KBOI) | Lazy F Ranch Airport (99OR) | 2026-08-09 07:42 UTC | 2026-08-09 08:23 UTC | 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
