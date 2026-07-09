# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--09_21:46:29_UTC-green)

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

**Latest saved flight:** 2026-07-09 21:46:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-09 21:46:29 UTC

- **134,889** saved flights
- **45,629** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **134,889** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,623,713.4 tonnes** estimated CO2 emissions
- **94,128,311 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5472 |
| 2 | SkyWest Airlines | 4966 |
| 3 | EJA | 2641 |
| 4 | IndiGo | 2498 |
| 5 | American Airlines | 2119 |
| 6 | Southwest Airlines | 2028 |
| 7 | ENY | 1693 |
| 8 | Delta Air Lines | 1611 |
| 9 | Lufthansa | 1388 |
| 10 | LATAM Airlines | 1237 |
| 11 | Vueling | 1178 |
| 12 | WIF | 1174 |
| 13 | AZU | 1148 |
| 14 | LXJ | 1035 |
| 15 | AXM | 1021 |
| 16 | Swiss International | 956 |
| 17 | All Nippon Airways | 878 |
| 18 | easyJet | 876 |
| 19 | Alaska Airlines | 857 |
| 20 | QLK | 842 |
| 21 | EJU | 831 |
| 22 | VIV | 743 |
| 23 | AEE | 733 |
| 24 | CXK | 728 |
| 25 | Cathay Pacific | 723 |
| 26 | Air France | 722 |
| 27 | United Airlines | 713 |
| 28 | JetBlue | 712 |
| 29 | MXY | 699 |
| 30 | GLO | 686 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 115789 |
| 2 | 🇪🇸 ES | 8939 |
| 3 | 🇮🇳 IN | 7837 |
| 4 | 🇦🇺 AU | 7772 |
| 5 | 🇧🇷 BR | 7591 |
| 6 | 🇨🇦 CA | 7129 |
| 7 | 🇩🇪 DE | 7027 |
| 8 | 🇮🇹 IT | 7004 |
| 9 | 🇬🇧 GB | 6072 |
| 10 | 🇯🇵 JP | 5755 |
| 11 | 🇫🇷 FR | 5358 |
| 12 | 🇨🇴 CO | 4226 |
| 13 | 🇲🇽 MX | 3925 |
| 14 | 🇬🇷 GR | 3849 |
| 15 | 🇳🇴 NO | 3659 |
| 16 | 🇨🇭 CH | 3486 |
| 17 | 🇹🇷 TR | 3078 |
| 18 | 🇲🇾 MY | 2651 |
| 19 | 🇵🇱 PL | 2228 |
| 20 | 🇿🇦 ZA | 2217 |
| 21 | 🇳🇿 NZ | 2107 |
| 22 | 🇹🇭 TH | 2064 |
| 23 | 🇰🇷 KR | 1984 |
| 24 | 🇵🇭 PH | 1850 |
| 25 | 🇬🇹 GT | 1827 |
| 26 | 🇲🇦 MA | 1426 |
| 27 | 🇲🇪 ME | 1342 |
| 28 | 🇳🇱 NL | 1260 |
| 29 | 🇭🇷 HR | 1201 |
| 30 | 🇲🇴 MO | 1186 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2808 |
| 2 | Denver International Airport |  | US | 2276 |
| 3 | Tokyo International Airport |  | JP | 1878 |
| 4 | Indira Gandhi International Airport |  | IN | 1733 |
| 5 | Harry Reid International Airport |  | US | 1680 |
| 6 | Guaymaral Airport |  | CO | 1647 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1579 |
| 8 | Zurich Airport |  | CH | 1499 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1428 |
| 10 | La Aurora Airport |  | GT | 1412 |
| 11 | Frankfurt am Main International Airport |  | DE | 1343 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1298 |
| 13 | Chicago O'Hare International Airport |  | US | 1283 |
| 14 | Salt Lake City International Airport |  | US | 1201 |
| 15 | El Dorado International Airport |  | CO | 1197 |
| 16 | Macau International Airport |  | MO | 1186 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1169 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1102 |
| 19 | Madrid Barajas International Airport |  | ES | 1102 |
| 20 | Capua Airport |  | IT | 1102 |
| 21 | Congonhas Airport |  | BR | 1076 |
| 22 | Kuala Lumpur International Airport |  | MY | 1030 |
| 23 | Charlotte/Douglas International Airport |  | US | 991 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 975 |
| 25 | Charles de Gaulle International Airport |  | FR | 964 |
| 26 | Bengaluru International Airport |  | IN | 944 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 925 |
| 28 | Malpensa International Airport |  | IT | 889 |
| 29 | Ninoy Aquino International Airport |  | PH | 861 |
| 30 | Daniel K Inouye International Airport |  | US | 838 |
| 31 | Barcelona International Airport |  | ES | 829 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 824 |
| 33 | Tenerife Norte Airport |  | ES | 807 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 793 |
| 35 | Calgary International Airport |  | CA | 780 |
| 36 | Seattle-Tacoma International Airport |  | US | 771 |
| 37 | Scottsdale Airport |  | US | 771 |
| 38 | Viracopos International Airport |  | BR | 767 |
| 39 | Vitoria/Foronda Airport |  | ES | 761 |
| 40 | Amsterdam Airport Schiphol |  | NL | 757 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 693 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 489 | 21m | 244 km | 2,059.0 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 338 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 333 | 24m | 225 km | 1,291.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 324 | 1h 10m | 770 km | 4,304.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 288 | 14m | 114 km | 564.9 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 251 | 26m | 275 km | 1,189.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 244 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 198 | 22m | 55 km | 188.2 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 188 | 44m | 241 km | 780.9 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 187 | 26m | 215 km | 692.6 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 185 | 20m | 99 km | 316.9 t |
| 17 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 182 | 1h 46m | 1,423 km | 4,466.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 180 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 175 | 27m | 152 km | 457.3 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 166 | 31m | 369 km | 1,056.6 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 163 | 20m | 250 km | 704.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 163 | 18m | 144 km | 405.5 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 161 | 30m | 49 km | 136.1 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 160 | 44m | 452 km | 1,247.0 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 158 | 1h 16m | 961 km | 2,618.9 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 157 | 1h 1m | 695 km | 1,882.0 t |
| 27 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 154 | 1h 38m | 1,156 km | 3,072.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 148 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N9713A |  | Wolf River Landing Strip (8WI5) | Wolf River Landing Strip (8WI5) | 2026-07-09 21:23 UTC | 2026-07-09 21:46 UTC | 23m |
| N3802C |  | Cortez Municipal Airport (KCEZ) | Tanner Field (CO27) | 2026-07-09 20:21 UTC | 2026-07-09 21:41 UTC | 1h 19m |
| DBB | DBB | Brisbane Archerfield Airport (YBAF) | Brisbane Archerfield Airport (YBAF) | 2026-07-09 21:07 UTC | 2026-07-09 21:39 UTC | 31m |
| CARD11 | CAR | Enix Airport (OK51) | Logsdon Ranch Airport (OK43) | 2026-07-09 21:26 UTC | 2026-07-09 21:37 UTC | 11m |
| LSXX | LSX | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-07-09 21:00 UTC | 2026-07-09 21:36 UTC | 36m |
| CXK557 | CXK | Ogden-Hinckley Airport (KOGD) | Wendover Airport (KENV) | 2026-07-09 20:47 UTC | 2026-07-09 21:32 UTC | 45m |
| BLUFF61 | BLU | 2TX3 (2TX3) | Anacacho Ranch Airport (0XS7) | 2026-07-09 21:16 UTC | 2026-07-09 21:32 UTC | 15m |
| N14HX |  | Blanding Municipal Airport (KBDG) | Blanding Municipal Airport (KBDG) | 2026-07-09 21:17 UTC | 2026-07-09 21:31 UTC | 13m |
| CPA234 | Cathay Pacific | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-07-09 11:06 UTC | 2026-07-09 21:30 UTC | 10h 24m |
| N4000K |  | Airlake Airport (KLVN) | Iowa City Municipal Airport (KIOW) | 2026-07-09 20:49 UTC | 2026-07-09 21:29 UTC | 39m |
| N700FP |  | Watsonville Municipal Airport (KWVI) | Lake Tahoe Airport (KTVL) | 2026-07-09 20:53 UTC | 2026-07-09 21:27 UTC | 34m |
| CKS252 | CKS | Cincinnati/Northern Kentucky International Airport (KCVG) | Grimshaw Airport (CFD5) | 2026-07-09 17:27 UTC | 2026-07-09 21:26 UTC | 3h 59m |
| CPA260 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-07-09 10:42 UTC | 2026-07-09 21:25 UTC | 10h 43m |
| N858DT |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-07-09 20:55 UTC | 2026-07-09 21:23 UTC | 28m |
| 19MF |  | Coleman A Young Municipal Airport (KDET) | Lakes Of The North Airport (K4Y4) | 2026-07-09 20:51 UTC | 2026-07-09 21:22 UTC | 31m |
| N716DB |  | Green Bay/Austin Straubel International Airport (KGRB) | Cedar Island Airport (WI10) | 2026-07-09 20:49 UTC | 2026-07-09 21:22 UTC | 32m |
| N742P |  | Minden-Tahoe Airport (KMEV) | Dayton Valley Airpark (KA34) | 2026-07-09 20:56 UTC | 2026-07-09 21:20 UTC | 23m |
| N888RK |  | Horseshoe Bay Resort Airport (KDZB) | Flying D Ranch Airport (73CO) | 2026-07-09 18:53 UTC | 2026-07-09 21:20 UTC | 2h 27m |
| N88765 |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-07-09 20:59 UTC | 2026-07-09 21:19 UTC | 20m |
| VILLN64 | VIL | Hill Afb Airport (KHIF) | Wendover Airport (KENV) | 2026-07-09 20:44 UTC | 2026-07-09 21:19 UTC | 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
