# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--31_20:25:30_UTC-green)

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

**Latest saved flight:** 2026-05-31 20:25:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-31 20:25:30 UTC

- **99,661** saved flights
- **35,450** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **99,661** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,220,644.6 tonnes** estimated CO2 emissions
- **70,762,006 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4142 |
| 2 | SkyWest Airlines | 3715 |
| 3 | IndiGo | 2021 |
| 4 | EJA | 1895 |
| 5 | American Airlines | 1612 |
| 6 | Southwest Airlines | 1504 |
| 7 | ENY | 1235 |
| 8 | Lufthansa | 1174 |
| 9 | Delta Air Lines | 1168 |
| 10 | Vueling | 936 |
| 11 | LATAM Airlines | 882 |
| 12 | WIF | 876 |
| 13 | AXM | 858 |
| 14 | AZU | 802 |
| 15 | LXJ | 753 |
| 16 | Swiss International | 731 |
| 17 | All Nippon Airways | 713 |
| 18 | Alaska Airlines | 696 |
| 19 | QLK | 674 |
| 20 | easyJet | 653 |
| 21 | EJU | 630 |
| 22 | Cathay Pacific | 593 |
| 23 | AEE | 588 |
| 24 | Air France | 580 |
| 25 | VIV | 578 |
| 26 | United Airlines | 557 |
| 27 | CXK | 538 |
| 28 | MXY | 532 |
| 29 | Japan Airlines | 500 |
| 30 | AXB | 495 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 83274 |
| 2 | 🇪🇸 ES | 6948 |
| 3 | 🇮🇳 IN | 6376 |
| 4 | 🇦🇺 AU | 5992 |
| 5 | 🇧🇷 BR | 5448 |
| 6 | 🇩🇪 DE | 5427 |
| 7 | 🇮🇹 IT | 5342 |
| 8 | 🇨🇦 CA | 5109 |
| 9 | 🇯🇵 JP | 4637 |
| 10 | 🇬🇧 GB | 4252 |
| 11 | 🇫🇷 FR | 4003 |
| 12 | 🇨🇴 CO | 3467 |
| 13 | 🇲🇽 MX | 3031 |
| 14 | 🇬🇷 GR | 2862 |
| 15 | 🇳🇴 NO | 2777 |
| 16 | 🇨🇭 CH | 2586 |
| 17 | 🇲🇾 MY | 2185 |
| 18 | 🇹🇷 TR | 1895 |
| 19 | 🇿🇦 ZA | 1751 |
| 20 | 🇳🇿 NZ | 1667 |
| 21 | 🇹🇭 TH | 1645 |
| 22 | 🇵🇱 PL | 1603 |
| 23 | 🇰🇷 KR | 1601 |
| 24 | 🇬🇹 GT | 1486 |
| 25 | 🇵🇭 PH | 1459 |
| 26 | 🇲🇦 MA | 1120 |
| 27 | 🇲🇴 MO | 1051 |
| 28 | 🇳🇱 NL | 1000 |
| 29 | 🇲🇪 ME | 957 |
| 30 | 🇭🇷 HR | 887 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2169 |
| 2 | Denver International Airport |  | US | 1699 |
| 3 | Tokyo International Airport |  | JP | 1534 |
| 4 | Indira Gandhi International Airport |  | IN | 1386 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1292 |
| 6 | Harry Reid International Airport |  | US | 1272 |
| 7 | Guaymaral Airport |  | CO | 1252 |
| 8 | Frankfurt am Main International Airport |  | DE | 1178 |
| 9 | Zurich Airport |  | CH | 1149 |
| 10 | La Aurora Airport |  | GT | 1142 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1074 |
| 12 | El Dorado International Airport |  | CO | 1066 |
| 13 | Macau International Airport |  | MO | 1051 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1012 |
| 15 | Chicago O'Hare International Airport |  | US | 997 |
| 16 | Madrid Barajas International Airport |  | ES | 875 |
| 17 | Kuala Lumpur International Airport |  | MY | 863 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 858 |
| 19 | Salt Lake City International Airport |  | US | 843 |
| 20 | Capua Airport |  | IT | 826 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 779 |
| 22 | Charlotte/Douglas International Airport |  | US | 771 |
| 23 | Charles de Gaulle International Airport |  | FR | 769 |
| 24 | Malpensa International Airport |  | IT | 765 |
| 25 | Bengaluru International Airport |  | IN | 764 |
| 26 | Congonhas Airport |  | BR | 756 |
| 27 | Daniel K Inouye International Airport |  | US | 691 |
| 28 | Tenerife Norte Airport |  | ES | 691 |
| 29 | Ninoy Aquino International Airport |  | PH | 666 |
| 30 | Barcelona International Airport |  | ES | 661 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 654 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 651 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 633 |
| 34 | Amsterdam Airport Schiphol |  | NL | 617 |
| 35 | Vitoria/Foronda Airport |  | ES | 611 |
| 36 | Don Mueang International Airport |  | TH | 603 |
| 37 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 38 | Calgary International Airport |  | CA | 584 |
| 39 | John Paul II International Airport Kraków-Balice Airport |  | PL | 573 |
| 40 | Seattle-Tacoma International Airport |  | US | 565 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 517 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 361 | 21m | 244 km | 1,520.1 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 268 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 263 | 24m | 225 km | 1,020.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 254 | 14m | 114 km | 498.2 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 244 | 1h 26m | 910 km | 3,828.9 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 243 | 28m | 304 km | 1,273.9 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 225 | 1h 10m | 770 km | 2,989.0 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 210 | 19m | 165 km | 597.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 197 | 26m | 275 km | 933.5 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 156 | 20m | 99 km | 267.2 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 149 | 27m | 215 km | 551.8 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 145 | 14m | 154 km | 384.2 t |
| 16 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 143 | 44m | 452 km | 1,114.5 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 141 | 22m | 55 km | 134.0 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 141 | 27m | 152 km | 368.5 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 134 | 20m | 250 km | 578.8 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 131 | 13m | - | - |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 130 | 20m | 147 km | 329.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 129 | 18m | 144 km | 320.9 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 126 | 1h 39m | 1,156 km | 2,513.7 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 124 | 1h 1m | 695 km | 1,486.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 119 | 1h 43m | 1,423 km | 2,920.4 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 115 | 1h 18m | 961 km | 1,906.2 t |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 30 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N844CK |  | Waco Regional Airport (KACT) | Brady-Pippin Airport (SN20) | 2026-05-31 18:23 UTC | 2026-05-31 20:25 UTC | 2h 1m |
| N608RH |  | Watts-Woodland Airport (KO41) | Watts-Woodland Airport (KO41) | 2026-05-31 18:32 UTC | 2026-05-31 20:20 UTC | 1h 47m |
| N690MF |  | Bb Airpark (TE88) | TE77 (TE77) | 2026-05-31 20:07 UTC | 2026-05-31 20:20 UTC | 12m |
| N780LA |  | Northeast Philadelphia Airport (KPNE) | Doylestown Airport (KDYL) | 2026-05-31 19:12 UTC | 2026-05-31 20:14 UTC | 1h 1m |
| N474S |  | 4AR5 (4AR5) | 4AR5 (4AR5) | 2026-05-31 19:21 UTC | 2026-05-31 20:13 UTC | 52m |
| N108J |  | AK18 (AK18) | Johnson Airport (3AK4) | 2026-05-31 19:36 UTC | 2026-05-31 20:13 UTC | 36m |
| N601FT |  | Deland Municipal-Sidney H Taylor Field (KDED) | North Exuma Airport (85FA) | 2026-05-31 19:29 UTC | 2026-05-31 20:12 UTC | 42m |
| PFT151 | PFT | Austin-Bergstrom International Airport (KAUS) | Van Nuys Airport (KVNY) | 2026-05-31 17:35 UTC | 2026-05-31 20:11 UTC | 2h 35m |
| N4922D |  | Montgomery-Gibbs Executive Airport (KMYF) | Hemet-Ryan Airport (KHMT) | 2026-05-31 19:26 UTC | 2026-05-31 20:11 UTC | 44m |
| BRG2661 | BRG | Ralph Wien Memorial Airport (PAOT) | Kivalina Airport (PAVL) | 2026-05-31 19:38 UTC | 2026-05-31 20:10 UTC | 32m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-05-31 19:58 UTC | 2026-05-31 20:10 UTC | 11m |
| CFXXN | CFX | Billings Logan International Airport (KBIL) | Calgary / Springbank Airport (CYBW) | 2026-05-31 18:44 UTC | 2026-05-31 20:09 UTC | 1h 24m |
| CXK1020 | CXK | Centennial Airport (KAPA) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-05-31 19:42 UTC | 2026-05-31 20:05 UTC | 23m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-05-31 19:50 UTC | 2026-05-31 20:05 UTC | 15m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-05-31 19:29 UTC | 2026-05-31 20:04 UTC | 35m |
| N4E |  | Camarillo Airport (KCMA) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-05-31 19:32 UTC | 2026-05-31 20:02 UTC | 30m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-05-31 19:49 UTC | 2026-05-31 20:01 UTC | 11m |
| N560PB |  | Scottsdale Airport (KSDL) | Parsons Field (4AZ6) | 2026-05-31 19:41 UTC | 2026-05-31 20:00 UTC | 19m |
| EJA285 | EJA | Los Angeles International Airport (KLAX) | K36U (K36U) | 2026-05-31 18:49 UTC | 2026-05-31 19:59 UTC | 1h 9m |
| N606LF |  | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-05-31 19:42 UTC | 2026-05-31 19:58 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
