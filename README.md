# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--07_12:58:44_UTC-green)

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

**Latest saved flight:** 2026-08-07 12:58:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-07 12:58:44 UTC

- **175,232** saved flights
- **56,592** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **175,232** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,109,452.2 tonnes** estimated CO2 emissions
- **122,287,082 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6953 |
| 2 | SkyWest Airlines | 6391 |
| 3 | EJA | 3459 |
| 4 | IndiGo | 3079 |
| 5 | Southwest Airlines | 2755 |
| 6 | American Airlines | 2736 |
| 7 | ENY | 2173 |
| 8 | Delta Air Lines | 2069 |
| 9 | LATAM Airlines | 1619 |
| 10 | Lufthansa | 1582 |
| 11 | AZU | 1548 |
| 12 | WIF | 1469 |
| 13 | Vueling | 1444 |
| 14 | LXJ | 1370 |
| 15 | AXM | 1196 |
| 16 | Swiss International | 1193 |
| 17 | easyJet | 1192 |
| 18 | QLK | 1082 |
| 19 | EJU | 1072 |
| 20 | All Nippon Airways | 1069 |
| 21 | Alaska Airlines | 1065 |
| 22 | VIV | 964 |
| 23 | Cathay Pacific | 944 |
| 24 | CXK | 928 |
| 25 | GLO | 921 |
| 26 | AEE | 916 |
| 27 | United Airlines | 907 |
| 28 | Air France | 903 |
| 29 | MXY | 882 |
| 30 | JetBlue | 869 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 150475 |
| 2 | 🇪🇸 ES | 11221 |
| 3 | 🇧🇷 BR | 9963 |
| 4 | 🇦🇺 AU | 9948 |
| 5 | 🇮🇳 IN | 9651 |
| 6 | 🇨🇦 CA | 9570 |
| 7 | 🇮🇹 IT | 9050 |
| 8 | 🇩🇪 DE | 8693 |
| 9 | 🇬🇧 GB | 8125 |
| 10 | 🇯🇵 JP | 7076 |
| 11 | 🇫🇷 FR | 6972 |
| 12 | 🇨🇴 CO | 6427 |
| 13 | 🇬🇷 GR | 5106 |
| 14 | 🇲🇽 MX | 5009 |
| 15 | 🇨🇭 CH | 4645 |
| 16 | 🇳🇴 NO | 4569 |
| 17 | 🇹🇷 TR | 4326 |
| 18 | 🇲🇾 MY | 3120 |
| 19 | 🇵🇱 PL | 2928 |
| 20 | 🇿🇦 ZA | 2852 |
| 21 | 🇹🇭 TH | 2611 |
| 22 | 🇳🇿 NZ | 2555 |
| 23 | 🇵🇭 PH | 2324 |
| 24 | 🇬🇹 GT | 2227 |
| 25 | 🇰🇷 KR | 2203 |
| 26 | 🇲🇦 MA | 1767 |
| 27 | 🇭🇷 HR | 1712 |
| 28 | 🇲🇪 ME | 1603 |
| 29 | 🇳🇱 NL | 1579 |
| 30 | 🇲🇴 MO | 1507 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3607 |
| 2 | Denver International Airport |  | US | 2891 |
| 3 | Tokyo International Airport |  | JP | 2208 |
| 4 | Guaymaral Airport |  | CO | 2163 |
| 5 | Indira Gandhi International Airport |  | IN | 2142 |
| 6 | Harry Reid International Airport |  | US | 2090 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1905 |
| 8 | Zurich Airport |  | CH | 1856 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1829 |
| 10 | La Aurora Airport |  | GT | 1714 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1605 |
| 12 | El Dorado International Airport |  | CO | 1581 |
| 13 | Chicago O'Hare International Airport |  | US | 1576 |
| 14 | Salt Lake City International Airport |  | US | 1565 |
| 15 | Frankfurt am Main International Airport |  | DE | 1543 |
| 16 | Macau International Airport |  | MO | 1507 |
| 17 | Congonhas Airport |  | BR | 1441 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1422 |
| 19 | Capua Airport |  | IT | 1368 |
| 20 | Madrid Barajas International Airport |  | ES | 1365 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1306 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1235 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1233 |
| 24 | Charlotte/Douglas International Airport |  | US | 1200 |
| 25 | Malpensa International Airport |  | IT | 1192 |
| 26 | Charles de Gaulle International Airport |  | FR | 1192 |
| 27 | Kuala Lumpur International Airport |  | MY | 1175 |
| 28 | Bengaluru International Airport |  | IN | 1146 |
| 29 | Ninoy Aquino International Airport |  | PH | 1093 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1084 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1082 |
| 32 | Barcelona International Airport |  | ES | 1038 |
| 33 | Daniel K Inouye International Airport |  | US | 1009 |
| 34 | Seattle-Tacoma International Airport |  | US | 1008 |
| 35 | Calgary International Airport |  | CA | 993 |
| 36 | Viracopos International Airport |  | BR | 992 |
| 37 | Reno/Tahoe International Airport |  | US | 991 |
| 38 | Oslo Gardermoen Airport |  | NO | 976 |
| 39 | Tenerife Norte Airport |  | ES | 966 |
| 40 | Amsterdam Airport Schiphol |  | NL | 950 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 895 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 640 | 21m | 244 km | 2,694.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 414 | 24m | 225 km | 1,606.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 407 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 406 | 1h 8m | 770 km | 5,393.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 323 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 294 | 27m | 275 km | 1,393.1 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 264 | 44m | 241 km | 1,096.6 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 262 | 22m | 55 km | 249.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 241 | 1h 48m | 1,423 km | 5,914.5 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 230 | 20m | 250 km | 993.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 224 | 26m | 215 km | 829.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 223 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 215 | 20m | 99 km | 368.3 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 209 | 50m | 556 km | 2,003.4 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 209 | 19m | 144 km | 519.9 t |
| 23 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 208 | 8m | - | - |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 207 | 1h 15m | 961 km | 3,431.1 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 205 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 204 | 1h 38m | 1,156 km | 4,069.7 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 203 | 31m | 369 km | 1,292.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 200 | 28m | 152 km | 522.7 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 199 | 24m | 218 km | 749.7 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 191 | 43m | 452 km | 1,488.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N215DS |  | Washington Manassas/Harry P Davis Field (KHEF) | Belmont Farm Airport (88VA) | 2026-08-07 11:45 UTC | 2026-08-07 12:58 UTC | 1h 12m |
| MOLOCH65 | MOL | Cognac-Chateaubernard (BA 709) Air Base (LFBG) | Cognac-Chateaubernard (BA 709) Air Base (LFBG) | 2026-08-07 12:33 UTC | 2026-08-07 12:55 UTC | 22m |
| N399GB |  | Ocean County Airport (KMJX) | Ocean County Airport (KMJX) | 2026-08-07 12:41 UTC | 2026-08-07 12:43 UTC | 2m |
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-08-07 12:22 UTC | 2026-08-07 12:40 UTC | 18m |
| N290VJ |  | Dillant/Hopkins Airport (KEEN) | Tweed/New Haven Airport (KHVN) | 2026-08-07 12:10 UTC | 2026-08-07 12:39 UTC | 29m |
| N2477T |  | Jim Sears Airport (3TA7) | Jim Sears Airport (3TA7) | 2026-08-07 12:19 UTC | 2026-08-07 12:29 UTC | 10m |
| ABX2044 | ABX | Cincinnati/Northern Kentucky International Airport (KCVG) | Austin-Bergstrom International Airport (KAUS) | 2026-08-07 10:24 UTC | 2026-08-07 12:28 UTC | 2h 4m |
| EJA608 | EJA | Laurence G Hanscom Field (KBED) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-08-07 11:34 UTC | 2026-08-07 12:25 UTC | 50m |
| PRF360 | PRF | RAF Cranwell (EGYD) | RAF Cranwell (EGYD) | 2026-08-07 11:50 UTC | 2026-08-07 12:25 UTC | 34m |
| HRT285 | HRT | Toronto Pearson International Airport (CYYZ) | Billy Bishop Toronto City Airport (CYTZ) | 2026-08-07 12:09 UTC | 2026-08-07 12:21 UTC | 11m |
| WIF170 | WIF | Bergen Airport Flesland (ENBR) | Sandane Airport Anda (ENSD) | 2026-08-07 11:54 UTC | 2026-08-07 12:20 UTC | 26m |
| CXK657 | CXK | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-08-07 11:56 UTC | 2026-08-07 12:20 UTC | 24m |
| JME633C | JME | Palma De Mallorca Airport (LEPA) | Nice-Cote d'Azur Airport (LFMN) | 2026-08-07 11:07 UTC | 2026-08-07 12:16 UTC | 1h 9m |
| SCU11 | SCU | Cherokee Ranch Airport (OK25) | Cherokee Ranch Airport (OK25) | 2026-08-07 11:55 UTC | 2026-08-07 12:11 UTC | 15m |
| HBZWE | HBZ | Courchevel Airport (LFLJ) | Raron Airport (LSTA) | 2026-08-07 10:41 UTC | 2026-08-07 12:11 UTC | 1h 29m |
| TIV525 | TIV | Boise Air Trml/Gowen Field (KBOI) | Plains Airport (KS34) | 2026-08-07 11:28 UTC | 2026-08-07 12:10 UTC | 42m |
| QRJ02 | QRJ | Ataturk International Airport (LTBA) | Skopje International Airport (LWSK) | 2026-08-07 11:09 UTC | 2026-08-07 12:08 UTC | 59m |
| N7260Q |  | Duda Airstrip (FA69) | Palm Beach County Park Airport (KLNA) | 2026-08-07 11:55 UTC | 2026-08-07 12:08 UTC | 12m |
| N79TV |  | Cochran Airport (K48A) | Cochran Airport (K48A) | 2026-08-07 11:51 UTC | 2026-08-07 12:08 UTC | 16m |
| CHX62 | CHX | Bautzen Airport (EDAB) | Pirna-Pratzschwitz Airport (EDAR) | 2026-08-07 11:49 UTC | 2026-08-07 12:02 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
