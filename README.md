# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--07_17:55:43_UTC-green)

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

**Latest saved flight:** 2026-08-07 17:55:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-07 17:55:43 UTC

- **176,103** saved flights
- **56,823** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **176,103** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,117,598.5 tonnes** estimated CO2 emissions
- **122,759,334 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6986 |
| 2 | SkyWest Airlines | 6417 |
| 3 | EJA | 3476 |
| 4 | IndiGo | 3091 |
| 5 | Southwest Airlines | 2770 |
| 6 | American Airlines | 2744 |
| 7 | ENY | 2189 |
| 8 | Delta Air Lines | 2080 |
| 9 | LATAM Airlines | 1628 |
| 10 | Lufthansa | 1584 |
| 11 | AZU | 1562 |
| 12 | WIF | 1478 |
| 13 | Vueling | 1453 |
| 14 | LXJ | 1383 |
| 15 | Swiss International | 1202 |
| 16 | AXM | 1196 |
| 17 | easyJet | 1193 |
| 18 | QLK | 1082 |
| 19 | EJU | 1079 |
| 20 | All Nippon Airways | 1069 |
| 21 | Alaska Airlines | 1066 |
| 22 | VIV | 966 |
| 23 | Cathay Pacific | 944 |
| 24 | CXK | 935 |
| 25 | GLO | 924 |
| 26 | AEE | 918 |
| 27 | Air France | 910 |
| 28 | United Airlines | 910 |
| 29 | MXY | 886 |
| 30 | JetBlue | 872 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 151305 |
| 2 | 🇪🇸 ES | 11281 |
| 3 | 🇧🇷 BR | 10022 |
| 4 | 🇦🇺 AU | 9951 |
| 5 | 🇮🇳 IN | 9687 |
| 6 | 🇨🇦 CA | 9632 |
| 7 | 🇮🇹 IT | 9104 |
| 8 | 🇩🇪 DE | 8735 |
| 9 | 🇬🇧 GB | 8153 |
| 10 | 🇯🇵 JP | 7076 |
| 11 | 🇫🇷 FR | 7007 |
| 12 | 🇨🇴 CO | 6466 |
| 13 | 🇬🇷 GR | 5132 |
| 14 | 🇲🇽 MX | 5029 |
| 15 | 🇨🇭 CH | 4674 |
| 16 | 🇳🇴 NO | 4594 |
| 17 | 🇹🇷 TR | 4364 |
| 18 | 🇲🇾 MY | 3120 |
| 19 | 🇵🇱 PL | 2932 |
| 20 | 🇿🇦 ZA | 2876 |
| 21 | 🇹🇭 TH | 2623 |
| 22 | 🇳🇿 NZ | 2555 |
| 23 | 🇵🇭 PH | 2326 |
| 24 | 🇬🇹 GT | 2246 |
| 25 | 🇰🇷 KR | 2203 |
| 26 | 🇲🇦 MA | 1779 |
| 27 | 🇭🇷 HR | 1727 |
| 28 | 🇲🇪 ME | 1605 |
| 29 | 🇳🇱 NL | 1588 |
| 30 | 🇲🇴 MO | 1507 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3631 |
| 2 | Denver International Airport |  | US | 2903 |
| 3 | Tokyo International Airport |  | JP | 2208 |
| 4 | Guaymaral Airport |  | CO | 2165 |
| 5 | Indira Gandhi International Airport |  | IN | 2152 |
| 6 | Harry Reid International Airport |  | US | 2098 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1910 |
| 8 | Zurich Airport |  | CH | 1871 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1840 |
| 10 | La Aurora Airport |  | GT | 1728 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1610 |
| 12 | Chicago O'Hare International Airport |  | US | 1585 |
| 13 | El Dorado International Airport |  | CO | 1581 |
| 14 | Salt Lake City International Airport |  | US | 1570 |
| 15 | Frankfurt am Main International Airport |  | DE | 1550 |
| 16 | Macau International Airport |  | MO | 1507 |
| 17 | Congonhas Airport |  | BR | 1451 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1424 |
| 19 | Capua Airport |  | IT | 1376 |
| 20 | Madrid Barajas International Airport |  | ES | 1371 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1312 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1238 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1235 |
| 24 | Charlotte/Douglas International Airport |  | US | 1204 |
| 25 | Malpensa International Airport |  | IT | 1200 |
| 26 | Charles de Gaulle International Airport |  | FR | 1199 |
| 27 | Kuala Lumpur International Airport |  | MY | 1175 |
| 28 | Bengaluru International Airport |  | IN | 1152 |
| 29 | Ninoy Aquino International Airport |  | PH | 1094 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1091 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1088 |
| 32 | Barcelona International Airport |  | ES | 1045 |
| 33 | Seattle-Tacoma International Airport |  | US | 1012 |
| 34 | Daniel K Inouye International Airport |  | US | 1011 |
| 35 | Viracopos International Airport |  | BR | 1001 |
| 36 | Reno/Tahoe International Airport |  | US | 999 |
| 37 | Calgary International Airport |  | CA | 997 |
| 38 | Oslo Gardermoen Airport |  | NO | 982 |
| 39 | Tenerife Norte Airport |  | ES | 968 |
| 40 | Amsterdam Airport Schiphol |  | NL | 955 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 895 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 642 | 21m | 244 km | 2,703.3 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 414 | 24m | 225 km | 1,606.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 411 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 406 | 1h 8m | 770 km | 5,393.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 325 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 296 | 27m | 275 km | 1,402.6 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 268 | 44m | 241 km | 1,113.2 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 243 | 1h 48m | 1,423 km | 5,963.6 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 230 | 20m | 250 km | 993.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 225 | 26m | 215 km | 833.3 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 225 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 218 | 31m | 49 km | 184.3 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 217 | 20m | 99 km | 371.7 t |
| 21 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 214 | 8m | - | - |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 212 | 51m | 556 km | 2,032.2 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 210 | 19m | 144 km | 522.4 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 209 | 1h 15m | 961 km | 3,464.3 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 205 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 204 | 1h 38m | 1,156 km | 4,069.7 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 203 | 31m | 369 km | 1,292.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 201 | 28m | 152 km | 525.3 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 200 | 24m | 218 km | 753.5 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 192 | 1h 2m | 695 km | 2,301.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RPA4600 | Republic Airways | Hartsfield/Jackson Atlanta International Airport (KATL) | Laguardia Airport (KLGA) | 2026-08-07 16:17 UTC | 2026-08-07 17:55 UTC | 1h 37m |
| N62F |  | Allegheny County Airport (KAGC) | Stitt Airport (PN59) | 2026-08-07 17:32 UTC | 2026-08-07 17:55 UTC | 23m |
| SH177 |  | Skypark Estates Owners Assoc Airport (18FD) | South Alabama Regional At Bill Benton Field (K79J) | 2026-08-07 17:33 UTC | 2026-08-07 17:54 UTC | 20m |
| N8312H |  | Byron Airport (KC83) | Byron Airport (KC83) | 2026-08-07 17:36 UTC | 2026-08-07 17:51 UTC | 14m |
| N99DQ |  | Republic Airport (KFRG) | Laguardia Airport (KLGA) | 2026-08-07 17:31 UTC | 2026-08-07 17:46 UTC | 15m |
| SH113 |  | Bob Sikes Airport (KCEW) | South Alabama Regional At Bill Benton Field (K79J) | 2026-08-07 17:33 UTC | 2026-08-07 17:44 UTC | 10m |
| N269FG |  | Trenton Mercer Airport (KTTN) | Northeast Philadelphia Airport (KPNE) | 2026-08-07 17:01 UTC | 2026-08-07 17:40 UTC | 38m |
| CXK678 | CXK | Montgomery-Gibbs Executive Airport (KMYF) | Riverside Airport (KRAL) | 2026-08-07 16:16 UTC | 2026-08-07 17:39 UTC | 1h 22m |
| AAL2220 | American Airlines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-07 15:46 UTC | 2026-08-07 17:39 UTC | 1h 53m |
| VICE13 | VIC | Rickenbacker International Airport (KLCK) | Rickenbacker International Airport (KLCK) | 2026-08-07 17:17 UTC | 2026-08-07 17:39 UTC | 22m |
| OXF1791 | OXF | Chandler Municipal Airport (KCHD) | Phoenix Goodyear Airport (KGYR) | 2026-08-07 17:12 UTC | 2026-08-07 17:37 UTC | 25m |
| TKJ5GM | TKJ | Sabiha Gokcen International Airport (LTFJ) | Trabzon International Airport (LTCG) | 2026-08-07 16:30 UTC | 2026-08-07 17:37 UTC | 1h 6m |
| N952JA |  | John Wayne/Orange County Airport (KSNA) | Fullerton Municipal Airport (KFUL) | 2026-08-07 16:49 UTC | 2026-08-07 17:36 UTC | 47m |
| OOI40 | OOI | Kiewit Airport (EBZH) | Schaffen Airport (EBDT) | 2026-08-07 17:09 UTC | 2026-08-07 17:35 UTC | 26m |
| VOID72 | VOI | Kickapoo Downtown Airport (KCWC) | Joseph Of Cupertino Stolport Airport (TS20) | 2026-08-07 17:16 UTC | 2026-08-07 17:35 UTC | 18m |
| TWY281 | TWY | Norman Y Mineta San Jose International Airport (KSJC) | Truckee-Tahoe Airport (KTRK) | 2026-08-07 17:05 UTC | 2026-08-07 17:35 UTC | 29m |
| PREY21 | PRE | Randolph Afb Airport (KRND) | Tee Pee Creek Airport (8TE0) | 2026-08-07 17:05 UTC | 2026-08-07 17:35 UTC | 29m |
| CHILD1 | CHI | CO54 (CO54) | CO98 (CO98) | 2026-08-07 17:10 UTC | 2026-08-07 17:34 UTC | 24m |
| PXT795 | PXT | Palm Springs International Airport (KPSP) | Buchanan Field (KCCR) | 2026-08-07 16:04 UTC | 2026-08-07 17:32 UTC | 1h 28m |
| JUMP17 | JUM | Carson Field (MT53) | Carson Field (MT53) | 2026-08-07 17:18 UTC | 2026-08-07 17:29 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
