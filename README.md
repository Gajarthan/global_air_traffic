# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--13_20:46:12_UTC-green)

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

**Latest saved flight:** 2026-06-13 20:46:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-13 20:46:12 UTC

- **109,529** saved flights
- **38,283** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **109,529** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,339,131.8 tonnes** estimated CO2 emissions
- **77,630,830 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4511 |
| 2 | SkyWest Airlines | 4099 |
| 3 | IndiGo | 2161 |
| 4 | EJA | 2107 |
| 5 | American Airlines | 1729 |
| 6 | Southwest Airlines | 1642 |
| 7 | ENY | 1361 |
| 8 | Delta Air Lines | 1293 |
| 9 | Lufthansa | 1239 |
| 10 | Vueling | 1005 |
| 11 | LATAM Airlines | 968 |
| 12 | WIF | 961 |
| 13 | AXM | 928 |
| 14 | AZU | 905 |
| 15 | LXJ | 828 |
| 16 | Swiss International | 794 |
| 17 | All Nippon Airways | 760 |
| 18 | Alaska Airlines | 746 |
| 19 | QLK | 723 |
| 20 | easyJet | 706 |
| 21 | EJU | 697 |
| 22 | Cathay Pacific | 655 |
| 23 | AEE | 622 |
| 24 | VIV | 619 |
| 25 | Air France | 618 |
| 26 | United Airlines | 606 |
| 27 | MXY | 586 |
| 28 | CXK | 576 |
| 29 | AXB | 541 |
| 30 | Japan Airlines | 537 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 92163 |
| 2 | 🇪🇸 ES | 7525 |
| 3 | 🇮🇳 IN | 6816 |
| 4 | 🇦🇺 AU | 6522 |
| 5 | 🇧🇷 BR | 6049 |
| 6 | 🇩🇪 DE | 5869 |
| 7 | 🇮🇹 IT | 5851 |
| 8 | 🇨🇦 CA | 5733 |
| 9 | 🇯🇵 JP | 4967 |
| 10 | 🇬🇧 GB | 4675 |
| 11 | 🇫🇷 FR | 4373 |
| 12 | 🇨🇴 CO | 3759 |
| 13 | 🇲🇽 MX | 3267 |
| 14 | 🇬🇷 GR | 3119 |
| 15 | 🇳🇴 NO | 3025 |
| 16 | 🇨🇭 CH | 2810 |
| 17 | 🇲🇾 MY | 2385 |
| 18 | 🇹🇷 TR | 2148 |
| 19 | 🇿🇦 ZA | 1871 |
| 20 | 🇰🇷 KR | 1828 |
| 21 | 🇹🇭 TH | 1803 |
| 22 | 🇵🇱 PL | 1800 |
| 23 | 🇳🇿 NZ | 1796 |
| 24 | 🇵🇭 PH | 1597 |
| 25 | 🇬🇹 GT | 1568 |
| 26 | 🇲🇦 MA | 1204 |
| 27 | 🇲🇴 MO | 1148 |
| 28 | 🇳🇱 NL | 1074 |
| 29 | 🇲🇪 ME | 1062 |
| 30 | 🇭🇷 HR | 955 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2350 |
| 2 | Denver International Airport |  | US | 1857 |
| 3 | Tokyo International Airport |  | JP | 1646 |
| 4 | Indira Gandhi International Airport |  | IN | 1481 |
| 5 | Guaymaral Airport |  | CO | 1393 |
| 6 | Harry Reid International Airport |  | US | 1388 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1369 |
| 8 | Zurich Airport |  | CH | 1239 |
| 9 | Frankfurt am Main International Airport |  | DE | 1223 |
| 10 | La Aurora Airport |  | GT | 1207 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1169 |
| 12 | Macau International Airport |  | MO | 1148 |
| 13 | El Dorado International Airport |  | CO | 1134 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1095 |
| 15 | Chicago O'Hare International Airport |  | US | 1087 |
| 16 | Madrid Barajas International Airport |  | ES | 956 |
| 17 | Capua Airport |  | IT | 938 |
| 18 | Kuala Lumpur International Airport |  | MY | 935 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 928 |
| 20 | Salt Lake City International Airport |  | US | 925 |
| 21 | Charlotte/Douglas International Airport |  | US | 845 |
| 22 | Congonhas Airport |  | BR | 837 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 830 |
| 24 | Bengaluru International Airport |  | IN | 825 |
| 25 | Charles de Gaulle International Airport |  | FR | 824 |
| 26 | Malpensa International Airport |  | IT | 801 |
| 27 | Ninoy Aquino International Airport |  | PH | 734 |
| 28 | Daniel K Inouye International Airport |  | US | 731 |
| 29 | Tenerife Norte Airport |  | ES | 728 |
| 30 | General Edward Lawrence Logan International Airport |  | US | 727 |
| 31 | Barcelona International Airport |  | ES | 720 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 713 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 702 |
| 34 | Amsterdam Airport Schiphol |  | NL | 664 |
| 35 | Don Mueang International Airport |  | TH | 657 |
| 36 | Vitoria/Foronda Airport |  | ES | 649 |
| 37 | Calgary International Airport |  | CA | 643 |
| 38 | Norman Y Mineta San Jose International Airport |  | US | 629 |
| 39 | Seattle-Tacoma International Airport |  | US | 628 |
| 40 | Viracopos International Airport |  | BR | 620 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 577 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 399 | 21m | 244 km | 1,680.1 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 292 | 24m | 225 km | 1,132.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 284 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 283 | 1h 7m | 706 km | 3,445.5 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 274 | 14m | 114 km | 537.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 266 | 1h 25m | 910 km | 4,174.2 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 256 | 1h 10m | 770 km | 3,400.8 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 224 | 19m | 165 km | 637.2 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 218 | 26m | 275 km | 1,033.0 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 209 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 162 | 20m | 99 km | 277.5 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 160 | 22m | 55 km | 152.1 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 158 | 27m | 215 km | 585.2 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 152 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 151 | 27m | 152 km | 394.6 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 148 | 31m | 369 km | 942.1 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 145 | 44m | 452 km | 1,130.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 143 | 18m | 144 km | 355.7 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 141 | 20m | 250 km | 609.0 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 133 | 1h 1m | 695 km | 1,594.3 t |
| 25 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 133 | 44m | 241 km | 552.5 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 131 | 1h 39m | 1,156 km | 2,613.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 130 | 1h 43m | 1,423 km | 3,190.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 124 | 1h 17m | 961 km | 2,055.4 t |
| 29 | Calgary International Airport (CYYC) | Moose Jaw Municipal Airport (CJS4) | 122 | 1h 2m | 611 km | 1,286.7 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N32BA |  | Grove City Airport (K29D) | Grove City Airport (K29D) | 2026-06-13 20:28 UTC | 2026-06-13 20:46 UTC | 18m |
| N40798 |  | Van Nuys Airport (KVNY) | Whiteman Airport (KWHP) | 2026-06-13 19:57 UTC | 2026-06-13 20:43 UTC | 46m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-06-13 20:18 UTC | 2026-06-13 20:35 UTC | 17m |
| XSN90 | XSN | Napa County Airport (KAPC) | Sacramento Mather Airport (KMHR) | 2026-06-13 20:16 UTC | 2026-06-13 20:33 UTC | 17m |
| N422LS |  | Purdue University Airport (KLAF) | Purdue University Airport (KLAF) | 2026-06-13 20:11 UTC | 2026-06-13 20:31 UTC | 20m |
| N6494Z |  | 89TA (89TA) | 89TA (89TA) | 2026-06-13 20:24 UTC | 2026-06-13 20:24 UTC | 0m |
| N10EA |  | Noahs Ark Airport (06MO) | Hillbillies Airport (72KS) | 2026-06-13 20:07 UTC | 2026-06-13 20:23 UTC | 15m |
| N4278L |  | Smyrna Airport (KMQY) | Smyrna Airport (KMQY) | 2026-06-13 20:19 UTC | 2026-06-13 20:22 UTC | 2m |
| N7891G |  | Long Beach (Daugherty Field) Airport (KLGB) | Fullerton Municipal Airport (KFUL) | 2026-06-13 19:26 UTC | 2026-06-13 20:18 UTC | 51m |
| N295SJ |  | Chino Airport (KCNO) | Mc Conville Airstrip (CA42) | 2026-06-13 19:22 UTC | 2026-06-13 20:18 UTC | 55m |
| N817SD |  | Van Nuys Airport (KVNY) | Meadows Field (KBFL) | 2026-06-13 19:47 UTC | 2026-06-13 20:17 UTC | 29m |
| N4278L |  | Smyrna Airport (KMQY) | Smyrna Airport (KMQY) | 2026-06-13 19:47 UTC | 2026-06-13 20:09 UTC | 22m |
| AYT101 | AYT | Hatzor Air Base (LLHS) | Mitzpe Ramon Airfield (LLMR) | 2026-06-13 19:52 UTC | 2026-06-13 20:09 UTC | 17m |
| N32AW |  | Kissimmee Gateway Airport (KISM) | Kissimmee Gateway Airport (KISM) | 2026-06-13 19:00 UTC | 2026-06-13 20:08 UTC | 1h 8m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-06-13 19:48 UTC | 2026-06-13 20:06 UTC | 17m |
| N243EA |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-06-13 17:21 UTC | 2026-06-13 20:06 UTC | 2h 44m |
| N617EL |  | Sheeley's Farm Airport (NK08) | Laurence G Hanscom Field (KBED) | 2026-06-13 19:10 UTC | 2026-06-13 20:06 UTC | 55m |
| N760VM |  | Minden-Tahoe Airport (KMEV) | Alpine County Airport (KM45) | 2026-06-13 18:49 UTC | 2026-06-13 20:05 UTC | 1h 15m |
| N681MA |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-06-13 19:27 UTC | 2026-06-13 20:04 UTC | 37m |
| N388WT |  | Richardson Field (XA23) | Mid-Way Regional Airport (KJWY) | 2026-06-13 19:38 UTC | 2026-06-13 20:03 UTC | 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
