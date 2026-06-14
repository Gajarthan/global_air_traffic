# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--14_18:48:33_UTC-green)

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

**Latest saved flight:** 2026-06-14 18:48:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-14 18:48:33 UTC

- **110,469** saved flights
- **38,543** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **110,469** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,350,409.0 tonnes** estimated CO2 emissions
- **78,284,580 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4567 |
| 2 | SkyWest Airlines | 4123 |
| 3 | IndiGo | 2173 |
| 4 | EJA | 2129 |
| 5 | American Airlines | 1738 |
| 6 | Southwest Airlines | 1654 |
| 7 | ENY | 1371 |
| 8 | Delta Air Lines | 1299 |
| 9 | Lufthansa | 1253 |
| 10 | Vueling | 1014 |
| 11 | LATAM Airlines | 975 |
| 12 | WIF | 974 |
| 13 | AXM | 933 |
| 14 | AZU | 913 |
| 15 | LXJ | 837 |
| 16 | Swiss International | 795 |
| 17 | All Nippon Airways | 769 |
| 18 | Alaska Airlines | 750 |
| 19 | QLK | 726 |
| 20 | easyJet | 710 |
| 21 | EJU | 704 |
| 22 | Cathay Pacific | 655 |
| 23 | AEE | 625 |
| 24 | VIV | 622 |
| 25 | Air France | 621 |
| 26 | United Airlines | 609 |
| 27 | MXY | 590 |
| 28 | CXK | 578 |
| 29 | AXB | 546 |
| 30 | Japan Airlines | 542 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 92820 |
| 2 | 🇪🇸 ES | 7595 |
| 3 | 🇮🇳 IN | 6852 |
| 4 | 🇦🇺 AU | 6569 |
| 5 | 🇧🇷 BR | 6089 |
| 6 | 🇮🇹 IT | 5962 |
| 7 | 🇩🇪 DE | 5923 |
| 8 | 🇨🇦 CA | 5780 |
| 9 | 🇯🇵 JP | 5015 |
| 10 | 🇬🇧 GB | 4736 |
| 11 | 🇫🇷 FR | 4431 |
| 12 | 🇨🇴 CO | 3761 |
| 13 | 🇲🇽 MX | 3279 |
| 14 | 🇬🇷 GR | 3148 |
| 15 | 🇳🇴 NO | 3061 |
| 16 | 🇨🇭 CH | 2833 |
| 17 | 🇲🇾 MY | 2409 |
| 18 | 🇹🇷 TR | 2192 |
| 19 | 🇿🇦 ZA | 1887 |
| 20 | 🇰🇷 KR | 1845 |
| 21 | 🇹🇭 TH | 1826 |
| 22 | 🇵🇱 PL | 1819 |
| 23 | 🇳🇿 NZ | 1807 |
| 24 | 🇵🇭 PH | 1611 |
| 25 | 🇬🇹 GT | 1578 |
| 26 | 🇲🇦 MA | 1217 |
| 27 | 🇲🇴 MO | 1149 |
| 28 | 🇳🇱 NL | 1083 |
| 29 | 🇲🇪 ME | 1083 |
| 30 | 🇭🇷 HR | 961 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2357 |
| 2 | Denver International Airport |  | US | 1865 |
| 3 | Tokyo International Airport |  | JP | 1661 |
| 4 | Indira Gandhi International Airport |  | IN | 1491 |
| 5 | Guaymaral Airport |  | CO | 1395 |
| 6 | Harry Reid International Airport |  | US | 1392 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1378 |
| 8 | Zurich Airport |  | CH | 1245 |
| 9 | Frankfurt am Main International Airport |  | DE | 1229 |
| 10 | La Aurora Airport |  | GT | 1214 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1180 |
| 12 | Macau International Airport |  | MO | 1149 |
| 13 | El Dorado International Airport |  | CO | 1134 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1098 |
| 15 | Chicago O'Hare International Airport |  | US | 1091 |
| 16 | Madrid Barajas International Airport |  | ES | 967 |
| 17 | Capua Airport |  | IT | 958 |
| 18 | Kuala Lumpur International Airport |  | MY | 940 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 933 |
| 20 | Salt Lake City International Airport |  | US | 932 |
| 21 | Charlotte/Douglas International Airport |  | US | 849 |
| 22 | Congonhas Airport |  | BR | 845 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 833 |
| 24 | Charles de Gaulle International Airport |  | FR | 832 |
| 25 | Bengaluru International Airport |  | IN | 828 |
| 26 | Malpensa International Airport |  | IT | 808 |
| 27 | General Edward Lawrence Logan International Airport |  | US | 747 |
| 28 | Ninoy Aquino International Airport |  | PH | 742 |
| 29 | Daniel K Inouye International Airport |  | US | 735 |
| 30 | Tenerife Norte Airport |  | ES | 731 |
| 31 | Barcelona International Airport |  | ES | 724 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 719 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 708 |
| 34 | Don Mueang International Airport |  | TH | 667 |
| 35 | Amsterdam Airport Schiphol |  | NL | 667 |
| 36 | Vitoria/Foronda Airport |  | ES | 657 |
| 37 | Calgary International Airport |  | CA | 649 |
| 38 | Seattle-Tacoma International Airport |  | US | 631 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 630 |
| 40 | Viracopos International Airport |  | BR | 623 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 578 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 403 | 21m | 244 km | 1,696.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 295 | 24m | 225 km | 1,144.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 286 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 283 | 1h 7m | 706 km | 3,445.5 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 274 | 14m | 114 km | 537.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 271 | 1h 25m | 910 km | 4,252.6 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 260 | 1h 10m | 770 km | 3,453.9 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 224 | 19m | 165 km | 637.2 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 220 | 26m | 275 km | 1,042.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 209 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 164 | 20m | 99 km | 280.9 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 161 | 22m | 55 km | 153.0 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 160 | 27m | 215 km | 592.6 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 156 | 13m | - | - |
| 17 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 151 | 27m | 152 km | 394.6 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 149 | 31m | 369 km | 948.4 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 147 | 44m | 452 km | 1,145.7 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 145 | 18m | 144 km | 360.7 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 141 | 20m | 250 km | 609.0 t |
| 23 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 139 | 44m | 241 km | 577.4 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 133 | 1h 1m | 695 km | 1,594.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 132 | 1h 43m | 1,423 km | 3,239.5 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 132 | 1h 39m | 1,156 km | 2,633.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 124 | 1h 17m | 961 km | 2,055.4 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 124 | 12m | - | - |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 123 | 24m | 223 km | 473.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N2838Q |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Auburn Municipal Airport (KAUN) | 2026-06-14 17:46 UTC | 2026-06-14 18:48 UTC | 1h 2m |
| EWG6NK | EWG | Cologne Bonn Airport (EDDK) | Olbia / Costa Smeralda Airport (LIEO) | 2026-06-14 17:13 UTC | 2026-06-14 18:47 UTC | 1h 33m |
| CGBGX | CGB | Langley Airport (CYNJ) | Fort Langley Airport (CBQ2) | 2026-06-14 18:28 UTC | 2026-06-14 18:45 UTC | 17m |
| AAL2529 | American Airlines | Charlotte/Douglas International Airport (KCLT) | Auburn Academy Airport (WA84) | 2026-06-14 13:35 UTC | 2026-06-14 18:41 UTC | 5h 6m |
| RJA403 | Royal Jordanian | Queen Alia International Airport (OJAI) | Queen Alia International Airport (OJAI) | 2026-06-14 14:39 UTC | 2026-06-14 18:38 UTC | 3h 59m |
| N58794 |  | Renton Municipal Airport (KRNT) | Renton Municipal Airport (KRNT) | 2026-06-14 18:03 UTC | 2026-06-14 18:36 UTC | 32m |
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-06-14 17:42 UTC | 2026-06-14 18:33 UTC | 51m |
| HZATS | HZA | Ataturk International Airport (LTBA) | Queen Alia International Airport (OJAI) | 2026-06-14 17:33 UTC | 2026-06-14 18:33 UTC | 1h 0m |
| AEZ7817 | AEZ | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Olbia / Costa Smeralda Airport (LIEO) | 2026-06-14 18:08 UTC | 2026-06-14 18:32 UTC | 24m |
| N682AC |  | Hidden Valley Ranch Airport (TS90) | Bb Airpark (TE88) | 2026-06-14 18:19 UTC | 2026-06-14 18:32 UTC | 13m |
| N7266D |  | Melbourne Orlando International Airport (KMLB) | New Smyrna Beach Municipal (Jack Bolt Field) Airport (KEVB) | 2026-06-14 17:51 UTC | 2026-06-14 18:28 UTC | 37m |
| N357LP |  | Greenville Spartanburg International Airport (KGSP) | Mountain Empire Airport (KMKJ) | 2026-06-14 17:57 UTC | 2026-06-14 18:27 UTC | 30m |
| PHX706 | PHX | Waukesha County Airport (KUES) | Thunder Bay Airport (CYQT) | 2026-06-14 17:06 UTC | 2026-06-14 18:27 UTC | 1h 21m |
| CNS308 | CNS | Morristown Municipal Airport (KMMU) | Deblois Flight Strip (K43B) | 2026-06-14 17:00 UTC | 2026-06-14 18:26 UTC | 1h 26m |
| N545BC |  | Zamperini Field (KTOA) | Meadows Field (KBFL) | 2026-06-14 17:07 UTC | 2026-06-14 18:21 UTC | 1h 14m |
| RJA144 | Royal Jordanian | Stockholm-Arlanda Airport (ESSA) | Queen Alia International Airport (OJAI) | 2026-06-14 14:25 UTC | 2026-06-14 18:20 UTC | 3h 54m |
| RJA108 | Royal Jordanian | Barcelona International Airport (LEBL) | Queen Alia International Airport (OJAI) | 2026-06-14 14:53 UTC | 2026-06-14 18:19 UTC | 3h 26m |
| UAE6RM | Emirates | Istanbul Airport (LTFM) | Queen Alia International Airport (OJAI) | 2026-06-14 17:05 UTC | 2026-06-14 18:18 UTC | 1h 13m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-06-14 17:36 UTC | 2026-06-14 18:16 UTC | 39m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-06-14 18:01 UTC | 2026-06-14 18:13 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
