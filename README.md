# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--17_12:29:25_UTC-green)

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

**Latest saved flight:** 2026-07-17 12:29:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-17 12:29:25 UTC

- **142,224** saved flights
- **47,715** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **142,224** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,706,763.6 tonnes** estimated CO2 emissions
- **98,942,820 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5786 |
| 2 | SkyWest Airlines | 5193 |
| 3 | EJA | 2797 |
| 4 | IndiGo | 2597 |
| 5 | American Airlines | 2269 |
| 6 | Southwest Airlines | 2142 |
| 7 | ENY | 1760 |
| 8 | Delta Air Lines | 1683 |
| 9 | Lufthansa | 1435 |
| 10 | LATAM Airlines | 1308 |
| 11 | Vueling | 1222 |
| 12 | AZU | 1221 |
| 13 | WIF | 1217 |
| 14 | LXJ | 1093 |
| 15 | AXM | 1054 |
| 16 | Swiss International | 1012 |
| 17 | easyJet | 926 |
| 18 | All Nippon Airways | 912 |
| 19 | Alaska Airlines | 896 |
| 20 | QLK | 894 |
| 21 | EJU | 877 |
| 22 | VIV | 790 |
| 23 | AEE | 761 |
| 24 | CXK | 759 |
| 25 | JetBlue | 759 |
| 26 | Air France | 758 |
| 27 | United Airlines | 741 |
| 28 | MXY | 736 |
| 29 | Cathay Pacific | 735 |
| 30 | GLO | 728 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 122261 |
| 2 | 🇪🇸 ES | 9283 |
| 3 | 🇦🇺 AU | 8152 |
| 4 | 🇮🇳 IN | 8137 |
| 5 | 🇧🇷 BR | 8025 |
| 6 | 🇨🇦 CA | 7482 |
| 7 | 🇮🇹 IT | 7418 |
| 8 | 🇩🇪 DE | 7381 |
| 9 | 🇬🇧 GB | 6506 |
| 10 | 🇯🇵 JP | 5971 |
| 11 | 🇫🇷 FR | 5661 |
| 12 | 🇨🇴 CO | 4539 |
| 13 | 🇲🇽 MX | 4125 |
| 14 | 🇬🇷 GR | 4052 |
| 15 | 🇳🇴 NO | 3810 |
| 16 | 🇨🇭 CH | 3681 |
| 17 | 🇹🇷 TR | 3367 |
| 18 | 🇲🇾 MY | 2749 |
| 19 | 🇵🇱 PL | 2386 |
| 20 | 🇿🇦 ZA | 2324 |
| 21 | 🇳🇿 NZ | 2182 |
| 22 | 🇹🇭 TH | 2125 |
| 23 | 🇰🇷 KR | 2026 |
| 24 | 🇵🇭 PH | 1926 |
| 25 | 🇬🇹 GT | 1867 |
| 26 | 🇲🇦 MA | 1489 |
| 27 | 🇲🇪 ME | 1408 |
| 28 | 🇳🇱 NL | 1342 |
| 29 | 🇭🇷 HR | 1295 |
| 30 | 🇲🇴 MO | 1192 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2923 |
| 2 | Denver International Airport |  | US | 2377 |
| 3 | Tokyo International Airport |  | JP | 1927 |
| 4 | Indira Gandhi International Airport |  | IN | 1804 |
| 5 | Harry Reid International Airport |  | US | 1786 |
| 6 | Guaymaral Airport |  | CO | 1731 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1632 |
| 8 | Zurich Airport |  | CH | 1580 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1489 |
| 10 | La Aurora Airport |  | GT | 1444 |
| 11 | Frankfurt am Main International Airport |  | DE | 1385 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1349 |
| 13 | Chicago O'Hare International Airport |  | US | 1330 |
| 14 | Salt Lake City International Airport |  | US | 1271 |
| 15 | El Dorado International Airport |  | CO | 1256 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1252 |
| 17 | Macau International Airport |  | MO | 1192 |
| 18 | Capua Airport |  | IT | 1164 |
| 19 | Madrid Barajas International Airport |  | ES | 1145 |
| 20 | Congonhas Airport |  | BR | 1143 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1129 |
| 22 | Kuala Lumpur International Airport |  | MY | 1061 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1034 |
| 24 | Charlotte/Douglas International Airport |  | US | 1028 |
| 25 | Charles de Gaulle International Airport |  | FR | 1004 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 991 |
| 27 | Bengaluru International Airport |  | IN | 972 |
| 28 | Malpensa International Airport |  | IT | 919 |
| 29 | Ninoy Aquino International Airport |  | PH | 899 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 871 |
| 31 | Daniel K Inouye International Airport |  | US | 868 |
| 32 | Barcelona International Airport |  | ES | 867 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 840 |
| 34 | Tenerife Norte Airport |  | ES | 823 |
| 35 | Calgary International Airport |  | CA | 811 |
| 36 | Seattle-Tacoma International Airport |  | US | 807 |
| 37 | Amsterdam Airport Schiphol |  | NL | 807 |
| 38 | Viracopos International Airport |  | BR | 805 |
| 39 | Scottsdale Airport |  | US | 803 |
| 40 | Vitoria/Foronda Airport |  | ES | 783 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 729 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 518 | 21m | 244 km | 2,181.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 349 | 24m | 225 km | 1,354.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 345 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 338 | 1h 9m | 770 km | 4,490.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 259 | 26m | 275 km | 1,227.3 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 254 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 208 | 22m | 55 km | 197.7 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 192 | 1h 46m | 1,423 km | 4,712.0 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 191 | 26m | 215 km | 707.4 t |
| 16 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 190 | 44m | 241 km | 789.2 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 189 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 189 | 20m | 99 km | 323.7 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 177 | 20m | 250 km | 764.5 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 177 | 28m | 152 km | 462.6 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 173 | 31m | 369 km | 1,101.2 t |
| 22 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 171 | 18m | 144 km | 425.4 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 167 | 44m | 452 km | 1,301.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 164 | 1h 1m | 695 km | 1,965.9 t |
| 26 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 164 | 1h 16m | 961 km | 2,718.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 163 | 1h 38m | 1,156 km | 3,251.8 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 159 | 13m | - | - |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 156 | 14m | 154 km | 413.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXK461 | CXK | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-07-17 12:13 UTC | 2026-07-17 12:29 UTC | 15m |
| N62TJ |  | Northern Colorado Regional Airport (KFNL) | Laramie Regional Airport (KLAR) | 2026-07-17 12:07 UTC | 2026-07-17 12:28 UTC | 20m |
| HBFXE | HBF | Olbia / Costa Smeralda Airport (LIEO) | Saanen Airport (LSGK) | 2026-07-17 10:53 UTC | 2026-07-17 12:26 UTC | 1h 33m |
| GCMLY | GCM | Henstridge Airfield (EGHS) | Henstridge Airfield (EGHS) | 2026-07-17 10:28 UTC | 2026-07-17 12:20 UTC | 1h 52m |
| AAL1605 | American Airlines | Ronald Reagan Washington Ntl Airport (KDCA) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-17 11:15 UTC | 2026-07-17 12:17 UTC | 1h 1m |
| NAK734M | NAK | Saint-Yan Airport (LFLN) | Clermont-Ferrand Auvergne Airport (LFLC) | 2026-07-17 11:53 UTC | 2026-07-17 12:17 UTC | 23m |
| N800SG |  | Bridgeport/Sikorsky Airport (KBDR) | Teterboro Airport (KTEB) | 2026-07-17 11:52 UTC | 2026-07-17 12:13 UTC | 20m |
| AAL700 | American Airlines | George Bush Intcntl/Houston Airport (KIAH) | Dallas-Fort Worth International Airport (KDFW) | 2026-07-17 11:23 UTC | 2026-07-17 12:10 UTC | 47m |
| AMU659 | AMU | Kaohsiung International Airport (RCKH) | Macau International Airport (VMMC) | 2026-07-17 11:14 UTC | 2026-07-17 12:10 UTC | 56m |
| HBZWD | HBZ | Saanen Airport (LSGK) | Reichenbach Air Base (LSGR) | 2026-07-17 11:07 UTC | 2026-07-17 12:09 UTC | 1h 2m |
| OCN517 | OCN | Palma De Mallorca Airport (LEPA) | Frankfurt am Main International Airport (EDDF) | 2026-07-17 10:18 UTC | 2026-07-17 12:06 UTC | 1h 47m |
| N539SF |  | KU77 (KU77) | KU77 (KU77) | 2026-07-17 11:32 UTC | 2026-07-17 12:02 UTC | 30m |
| DESERT8 | DES | Julian Hinds Pump Plant Airstrip (73CL) | Lake Havasu City Airport (KHII) | 2026-07-17 11:22 UTC | 2026-07-17 11:57 UTC | 34m |
| N721GT |  | Centennial Airport (KAPA) | CO86 (CO86) | 2026-07-17 11:38 UTC | 2026-07-17 11:56 UTC | 18m |
| HK2078G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-07-17 11:32 UTC | 2026-07-17 11:52 UTC | 20m |
| AEE260 | AEE | Eleftherios Venizelos International Airport (LGAV) | Limnos Airport (LGLM) | 2026-07-17 11:10 UTC | 2026-07-17 11:50 UTC | 40m |
| SHT1480 | SHT | London Gatwick Airport (EGKK) | Glasgow International Airport (EGPF) | 2026-07-17 10:36 UTC | 2026-07-17 11:48 UTC | 1h 12m |
| OEGGM | OEG | Paris-Le Bourget Airport (LFPB) | Samedan Airport (LSZS) | 2026-07-17 10:50 UTC | 2026-07-17 11:43 UTC | 52m |
| N1439Y |  | Punta Gorda Airport (KPGD) | Punta Gorda Airport (KPGD) | 2026-07-17 11:35 UTC | 2026-07-17 11:43 UTC | 7m |
| RYR3FD | Ryanair | Gdańsk Lech Wałęsa Airport (EPGD) | Chania International Airport (LGSA) | 2026-07-17 09:07 UTC | 2026-07-17 11:41 UTC | 2h 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
