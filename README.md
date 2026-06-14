# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--14_12:02:05_UTC-green)

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

**Latest saved flight:** 2026-06-14 12:02:05 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-14 12:02:05 UTC

- **109,921** saved flights
- **38,369** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **109,921** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,343,892.5 tonnes** estimated CO2 emissions
- **77,906,813 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4535 |
| 2 | SkyWest Airlines | 4110 |
| 3 | IndiGo | 2166 |
| 4 | EJA | 2107 |
| 5 | American Airlines | 1732 |
| 6 | Southwest Airlines | 1647 |
| 7 | ENY | 1362 |
| 8 | Delta Air Lines | 1296 |
| 9 | Lufthansa | 1247 |
| 10 | Vueling | 1008 |
| 11 | LATAM Airlines | 970 |
| 12 | WIF | 967 |
| 13 | AXM | 933 |
| 14 | AZU | 906 |
| 15 | LXJ | 828 |
| 16 | Swiss International | 794 |
| 17 | All Nippon Airways | 769 |
| 18 | Alaska Airlines | 750 |
| 19 | QLK | 726 |
| 20 | easyJet | 709 |
| 21 | EJU | 702 |
| 22 | Cathay Pacific | 655 |
| 23 | AEE | 623 |
| 24 | VIV | 619 |
| 25 | Air France | 618 |
| 26 | United Airlines | 607 |
| 27 | MXY | 586 |
| 28 | CXK | 577 |
| 29 | AXB | 543 |
| 30 | Japan Airlines | 542 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 92296 |
| 2 | 🇪🇸 ES | 7554 |
| 3 | 🇮🇳 IN | 6834 |
| 4 | 🇦🇺 AU | 6567 |
| 5 | 🇧🇷 BR | 6054 |
| 6 | 🇩🇪 DE | 5896 |
| 7 | 🇮🇹 IT | 5896 |
| 8 | 🇨🇦 CA | 5752 |
| 9 | 🇯🇵 JP | 5015 |
| 10 | 🇬🇧 GB | 4711 |
| 11 | 🇫🇷 FR | 4404 |
| 12 | 🇨🇴 CO | 3759 |
| 13 | 🇲🇽 MX | 3267 |
| 14 | 🇬🇷 GR | 3132 |
| 15 | 🇳🇴 NO | 3041 |
| 16 | 🇨🇭 CH | 2821 |
| 17 | 🇲🇾 MY | 2409 |
| 18 | 🇹🇷 TR | 2163 |
| 19 | 🇿🇦 ZA | 1885 |
| 20 | 🇰🇷 KR | 1845 |
| 21 | 🇹🇭 TH | 1826 |
| 22 | 🇵🇱 PL | 1808 |
| 23 | 🇳🇿 NZ | 1807 |
| 24 | 🇵🇭 PH | 1611 |
| 25 | 🇬🇹 GT | 1570 |
| 26 | 🇲🇦 MA | 1211 |
| 27 | 🇲🇴 MO | 1149 |
| 28 | 🇳🇱 NL | 1079 |
| 29 | 🇲🇪 ME | 1074 |
| 30 | 🇭🇷 HR | 957 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2354 |
| 2 | Denver International Airport |  | US | 1861 |
| 3 | Tokyo International Airport |  | JP | 1661 |
| 4 | Indira Gandhi International Airport |  | IN | 1485 |
| 5 | Guaymaral Airport |  | CO | 1393 |
| 6 | Harry Reid International Airport |  | US | 1388 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1374 |
| 8 | Zurich Airport |  | CH | 1241 |
| 9 | Frankfurt am Main International Airport |  | DE | 1225 |
| 10 | La Aurora Airport |  | GT | 1208 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1173 |
| 12 | Macau International Airport |  | MO | 1149 |
| 13 | El Dorado International Airport |  | CO | 1134 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1098 |
| 15 | Chicago O'Hare International Airport |  | US | 1088 |
| 16 | Madrid Barajas International Airport |  | ES | 960 |
| 17 | Capua Airport |  | IT | 946 |
| 18 | Kuala Lumpur International Airport |  | MY | 940 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 930 |
| 20 | Salt Lake City International Airport |  | US | 927 |
| 21 | Charlotte/Douglas International Airport |  | US | 845 |
| 22 | Congonhas Airport |  | BR | 838 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 833 |
| 24 | Bengaluru International Airport |  | IN | 827 |
| 25 | Charles de Gaulle International Airport |  | FR | 826 |
| 26 | Malpensa International Airport |  | IT | 802 |
| 27 | Ninoy Aquino International Airport |  | PH | 742 |
| 28 | Daniel K Inouye International Airport |  | US | 734 |
| 29 | General Edward Lawrence Logan International Airport |  | US | 731 |
| 30 | Tenerife Norte Airport |  | ES | 730 |
| 31 | Barcelona International Airport |  | ES | 721 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 714 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 702 |
| 34 | Don Mueang International Airport |  | TH | 667 |
| 35 | Amsterdam Airport Schiphol |  | NL | 665 |
| 36 | Vitoria/Foronda Airport |  | ES | 651 |
| 37 | Calgary International Airport |  | CA | 648 |
| 38 | Seattle-Tacoma International Airport |  | US | 631 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 629 |
| 40 | Viracopos International Airport |  | BR | 620 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 577 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 402 | 21m | 244 km | 1,692.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 295 | 24m | 225 km | 1,144.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 284 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 283 | 1h 7m | 706 km | 3,445.5 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 274 | 14m | 114 km | 537.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 271 | 1h 25m | 910 km | 4,252.6 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 260 | 1h 10m | 770 km | 3,453.9 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 224 | 19m | 165 km | 637.2 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 219 | 26m | 275 km | 1,037.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 209 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 163 | 20m | 99 km | 279.2 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 160 | 22m | 55 km | 152.1 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 159 | 27m | 215 km | 588.9 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 155 | 13m | - | - |
| 17 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 151 | 27m | 152 km | 394.6 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 149 | 31m | 369 km | 948.4 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 147 | 44m | 452 km | 1,145.7 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 144 | 18m | 144 km | 358.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 141 | 20m | 250 km | 609.0 t |
| 23 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 135 | 44m | 241 km | 560.8 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 133 | 1h 1m | 695 km | 1,594.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 131 | 1h 43m | 1,423 km | 3,214.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 131 | 1h 39m | 1,156 km | 2,613.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 124 | 1h 17m | 961 km | 2,055.4 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 123 | 12m | - | - |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 122 | 24m | 223 km | 469.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| IFJ32A | IFJ | Viseu Airport (LPVZ) | Viseu Airport (LPVZ) | 2026-06-14 11:09 UTC | 2026-06-14 12:02 UTC | 52m |
| CXK461 | CXK | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-06-14 11:27 UTC | 2026-06-14 11:52 UTC | 25m |
| N902TV |  | Leesburg Executive Airport (KJYO) | Lancaster Airport (KLNS) | 2026-06-14 11:07 UTC | 2026-06-14 11:49 UTC | 41m |
| HBZWD | HBZ | Bern Belp Airport (LSZB) | Raron Airport (LSTA) | 2026-06-14 11:11 UTC | 2026-06-14 11:28 UTC | 16m |
| TJD850 | TJD | Lisbon Portela Airport (LPPT) | Nice-Cote d'Azur Airport (LFMN) | 2026-06-14 09:22 UTC | 2026-06-14 11:27 UTC | 2h 5m |
| BOX713 | BOX | Chek Lap Kok International Airport (VHHH) | Queen Alia International Airport (OJAI) | 2026-06-13 22:49 UTC | 2026-06-14 11:19 UTC | 12h 30m |
| FD535 |  | Adelaide International Airport (YPAD) | Callendale Airport (YCLE) | 2026-06-14 10:35 UTC | 2026-06-14 11:16 UTC | 41m |
| EJU65WF | EJU | Francisco de Sá Carneiro Airport (LPPR) | Capua Airport (LIAU) | 2026-06-14 08:48 UTC | 2026-06-14 11:15 UTC | 2h 26m |
| PH980 |  | De Peel Air Base (EHDP) | De Peel Air Base (EHDP) | 2026-06-14 10:36 UTC | 2026-06-14 11:14 UTC | 37m |
| TAM8161 | LATAM Airlines | Ministro Pistarini International Airport (SAEZ) | Jose Mucio Monteiro Airport (SIRF) | 2026-06-14 06:54 UTC | 2026-06-14 11:12 UTC | 4h 17m |
| CAP3534 | CAP | Holloman Afb Airport (KHMN) | KWSD (KWSD) | 2026-06-14 10:29 UTC | 2026-06-14 11:11 UTC | 42m |
| RYR177D | Ryanair | Brussels South Charleroi Airport (EBCI) | Vitoria/Foronda Airport (LEVT) | 2026-06-14 09:50 UTC | 2026-06-14 11:11 UTC | 1h 21m |
| HB3395 |  | Bad Ragaz Airport (LSZE) | Samedan Airport (LSZS) | 2026-06-14 09:13 UTC | 2026-06-14 11:10 UTC | 1h 56m |
| 3AMAC |  | Cannes-Mandelieu Airport (LFMD) | Nice-Cote d'Azur Airport (LFMN) | 2026-06-14 10:35 UTC | 2026-06-14 11:09 UTC | 34m |
| EWG43Q | EWG | Dionysios Solomos Airport (LGZA) | Hamburg Airport (EDDH) | 2026-06-14 08:07 UTC | 2026-06-14 11:08 UTC | 3h 0m |
| RYR6GM | Ryanair | Memmingen Allgau Airport (EDJA) | Visoko Sport Airfield (LQVI) | 2026-06-14 10:12 UTC | 2026-06-14 11:08 UTC | 55m |
| EAI64B | EAI | Dublin Airport (EIDW) | Birmingham International Airport (EGBB) | 2026-06-14 10:16 UTC | 2026-06-14 11:07 UTC | 51m |
| LLR513 | LLR | Bengaluru International Airport (VOBL) | Hosur Airport (VO95) | 2026-06-14 10:46 UTC | 2026-06-14 11:07 UTC | 21m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-06-14 10:06 UTC | 2026-06-14 10:58 UTC | 52m |
| RYR9023 | Ryanair | Dole-Tavaux Airport (LFGJ) | Saiss Airport (GMFF) | 2026-06-14 08:43 UTC | 2026-06-14 10:58 UTC | 2h 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
