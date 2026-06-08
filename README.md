# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--08_20:24:27_UTC-green)

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

**Latest saved flight:** 2026-06-08 20:24:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-08 20:24:27 UTC

- **106,519** saved flights
- **37,421** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **106,519** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,302,289.8 tonnes** estimated CO2 emissions
- **75,495,059 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4393 |
| 2 | SkyWest Airlines | 4007 |
| 3 | IndiGo | 2111 |
| 4 | EJA | 2046 |
| 5 | American Airlines | 1706 |
| 6 | Southwest Airlines | 1607 |
| 7 | ENY | 1335 |
| 8 | Delta Air Lines | 1267 |
| 9 | Lufthansa | 1218 |
| 10 | Vueling | 980 |
| 11 | LATAM Airlines | 943 |
| 12 | WIF | 934 |
| 13 | AXM | 910 |
| 14 | AZU | 864 |
| 15 | LXJ | 803 |
| 16 | Swiss International | 775 |
| 17 | All Nippon Airways | 741 |
| 18 | Alaska Airlines | 734 |
| 19 | QLK | 710 |
| 20 | easyJet | 690 |
| 21 | EJU | 680 |
| 22 | Cathay Pacific | 633 |
| 23 | AEE | 613 |
| 24 | Air France | 608 |
| 25 | VIV | 608 |
| 26 | United Airlines | 587 |
| 27 | MXY | 579 |
| 28 | CXK | 560 |
| 29 | Japan Airlines | 526 |
| 30 | AXB | 522 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 89583 |
| 2 | 🇪🇸 ES | 7324 |
| 3 | 🇮🇳 IN | 6659 |
| 4 | 🇦🇺 AU | 6389 |
| 5 | 🇧🇷 BR | 5845 |
| 6 | 🇩🇪 DE | 5720 |
| 7 | 🇮🇹 IT | 5713 |
| 8 | 🇨🇦 CA | 5549 |
| 9 | 🇯🇵 JP | 4874 |
| 10 | 🇬🇧 GB | 4519 |
| 11 | 🇫🇷 FR | 4234 |
| 12 | 🇨🇴 CO | 3661 |
| 13 | 🇲🇽 MX | 3190 |
| 14 | 🇬🇷 GR | 3029 |
| 15 | 🇳🇴 NO | 2955 |
| 16 | 🇨🇭 CH | 2723 |
| 17 | 🇲🇾 MY | 2336 |
| 18 | 🇹🇷 TR | 2061 |
| 19 | 🇿🇦 ZA | 1836 |
| 20 | 🇰🇷 KR | 1773 |
| 21 | 🇳🇿 NZ | 1766 |
| 22 | 🇹🇭 TH | 1759 |
| 23 | 🇵🇱 PL | 1743 |
| 24 | 🇵🇭 PH | 1567 |
| 25 | 🇬🇹 GT | 1539 |
| 26 | 🇲🇦 MA | 1177 |
| 27 | 🇲🇴 MO | 1108 |
| 28 | 🇳🇱 NL | 1046 |
| 29 | 🇲🇪 ME | 1024 |
| 30 | 🇭🇷 HR | 928 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2308 |
| 2 | Denver International Airport |  | US | 1816 |
| 3 | Tokyo International Airport |  | JP | 1613 |
| 4 | Indira Gandhi International Airport |  | IN | 1448 |
| 5 | Harry Reid International Airport |  | US | 1359 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1341 |
| 7 | Guaymaral Airport |  | CO | 1335 |
| 8 | Zurich Airport |  | CH | 1210 |
| 9 | Frankfurt am Main International Airport |  | DE | 1207 |
| 10 | La Aurora Airport |  | GT | 1184 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1152 |
| 12 | El Dorado International Airport |  | CO | 1116 |
| 13 | Macau International Airport |  | MO | 1108 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1074 |
| 15 | Chicago O'Hare International Airport |  | US | 1070 |
| 16 | Madrid Barajas International Airport |  | ES | 930 |
| 17 | Kuala Lumpur International Airport |  | MY | 915 |
| 18 | Salt Lake City International Airport |  | US | 910 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 910 |
| 20 | Capua Airport |  | IT | 910 |
| 21 | Charlotte/Douglas International Airport |  | US | 827 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 814 |
| 23 | Charles de Gaulle International Airport |  | FR | 809 |
| 24 | Congonhas Airport |  | BR | 809 |
| 25 | Bengaluru International Airport |  | IN | 797 |
| 26 | Malpensa International Airport |  | IT | 796 |
| 27 | Daniel K Inouye International Airport |  | US | 723 |
| 28 | Ninoy Aquino International Airport |  | PH | 718 |
| 29 | Tenerife Norte Airport |  | ES | 718 |
| 30 | Barcelona International Airport |  | ES | 699 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 689 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 688 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 685 |
| 34 | Amsterdam Airport Schiphol |  | NL | 647 |
| 35 | Don Mueang International Airport |  | TH | 643 |
| 36 | Vitoria/Foronda Airport |  | ES | 637 |
| 37 | Calgary International Airport |  | CA | 629 |
| 38 | Seattle-Tacoma International Airport |  | US | 616 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 612 |
| 40 | Netaji Subhash Chandra Bose International Airport |  | IN | 607 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 551 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 391 | 21m | 244 km | 1,646.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 284 | 24m | 225 km | 1,101.8 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 281 | 1h 7m | 706 km | 3,421.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 277 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 268 | 14m | 114 km | 525.6 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 260 | 1h 25m | 910 km | 4,080.0 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 259 | 28m | 304 km | 1,357.7 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 245 | 1h 10m | 770 km | 3,254.6 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 220 | 19m | 165 km | 625.8 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 213 | 26m | 275 km | 1,009.3 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 205 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 161 | 20m | 99 km | 275.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 155 | 27m | 215 km | 574.1 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 150 | 14m | 154 km | 397.4 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 148 | 27m | 152 km | 386.8 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 147 | 31m | 369 km | 935.7 t |
| 19 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 145 | 44m | 452 km | 1,130.1 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 144 | 13m | - | - |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 140 | 18m | 144 km | 348.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 130 | 1h 1m | 695 km | 1,558.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 125 | 1h 43m | 1,423 km | 3,067.7 t |
| 27 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 125 | 44m | 241 km | 519.2 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 52m | 1,304 km | 2,722.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 119 | 1h 18m | 961 km | 1,972.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N2060U |  | Zamperini Field (KTOA) | Zamperini Field (KTOA) | 2026-06-08 19:32 UTC | 2026-06-08 20:24 UTC | 51m |
| N52NL |  | Provo Municipal Airport (KPVU) | UT99 (UT99) | 2026-06-08 20:06 UTC | 2026-06-08 20:23 UTC | 17m |
| N431SL |  | 42MI (42MI) | Oakland/Troy Airport (KVLL) | 2026-06-08 19:44 UTC | 2026-06-08 20:20 UTC | 36m |
| N90508 |  | Brookneal/Campbell County Airport (K0V4) | Breezy Knoll Airport (VA13) | 2026-06-08 20:01 UTC | 2026-06-08 20:20 UTC | 19m |
| R21234 |  | Ladd Army Air Field (PAFB) | Lakloey Air Park (AK22) | 2026-06-08 19:27 UTC | 2026-06-08 20:15 UTC | 48m |
| KING41 | KIN | Patrick Space Force Base Airport (KCOF) | Patrick Space Force Base Airport (KCOF) | 2026-06-08 18:59 UTC | 2026-06-08 20:13 UTC | 1h 14m |
| N107MW |  | Marshdale Airport (CO52) | Marshdale Airport (CO52) | 2026-06-08 18:39 UTC | 2026-06-08 20:12 UTC | 1h 33m |
| N27DX |  | Republic Airport (KFRG) | Francis S Gabreski Airport (KFOK) | 2026-06-08 19:33 UTC | 2026-06-08 20:06 UTC | 32m |
| N622TP |  | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-06-08 19:37 UTC | 2026-06-08 20:05 UTC | 28m |
| WNG16E | WNG | Denton Enterprise Airport (KDTO) | Dreamland Airport (XA48) | 2026-06-08 19:35 UTC | 2026-06-08 20:02 UTC | 26m |
| FTO388 | FTO | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-06-08 19:30 UTC | 2026-06-08 20:01 UTC | 30m |
| N1895J |  | East Penn Airport (PA30) | Allentown Queen City Municipal Airport (KXLL) | 2026-06-08 19:45 UTC | 2026-06-08 19:59 UTC | 14m |
| LXP285 | LXP | Comodoro Arturo Merino Benitez International Airport (SCEL) | Teniente Vidal Airport (SCCY) | 2026-06-08 15:59 UTC | 2026-06-08 19:57 UTC | 3h 57m |
| N52858 |  | Camarillo Airport (KCMA) | Riverside Airport (KRAL) | 2026-06-08 18:55 UTC | 2026-06-08 19:55 UTC | 1h 0m |
| N307FF |  | Keflavik International Airport (BIKF) | Bangor International Airport (KBGR) | 2026-06-08 15:40 UTC | 2026-06-08 19:55 UTC | 4h 14m |
| BLKWG42 | BLK | 44GA (44GA) | Crisp County-Cordele Airport (KCKF) | 2026-06-08 17:34 UTC | 2026-06-08 19:55 UTC | 2h 20m |
| JEDI2 | JED | NC47 (NC47) | Billy Mitchell Airport (KHSE) | 2026-06-08 19:42 UTC | 2026-06-08 19:54 UTC | 11m |
| WIF149 | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-06-08 19:12 UTC | 2026-06-08 19:48 UTC | 36m |
| N6TM |  | KS98 (KS98) | Crystal Springs Ranch Airport (UT54) | 2026-06-08 18:15 UTC | 2026-06-08 19:46 UTC | 1h 30m |
| XCEDM | XCE | Licenciado Adolfo Lopez Mateos International Airport (MMTO) | Atizapan De Zaragoza Airport (MMJC) | 2026-06-08 19:40 UTC | 2026-06-08 19:45 UTC | 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
