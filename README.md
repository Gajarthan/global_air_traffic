# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--13_15:00:20_UTC-green)

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

**Latest saved flight:** 2026-06-13 15:00:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-13 15:00:20 UTC

- **109,353** saved flights
- **38,226** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **109,353** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,336,945.2 tonnes** estimated CO2 emissions
- **77,504,070 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4502 |
| 2 | SkyWest Airlines | 4083 |
| 3 | IndiGo | 2161 |
| 4 | EJA | 2102 |
| 5 | American Airlines | 1726 |
| 6 | Southwest Airlines | 1636 |
| 7 | ENY | 1358 |
| 8 | Delta Air Lines | 1291 |
| 9 | Lufthansa | 1239 |
| 10 | Vueling | 1003 |
| 11 | LATAM Airlines | 968 |
| 12 | WIF | 961 |
| 13 | AXM | 928 |
| 14 | AZU | 905 |
| 15 | LXJ | 826 |
| 16 | Swiss International | 793 |
| 17 | All Nippon Airways | 760 |
| 18 | Alaska Airlines | 744 |
| 19 | QLK | 723 |
| 20 | easyJet | 706 |
| 21 | EJU | 697 |
| 22 | Cathay Pacific | 655 |
| 23 | AEE | 622 |
| 24 | VIV | 619 |
| 25 | Air France | 618 |
| 26 | United Airlines | 603 |
| 27 | MXY | 585 |
| 28 | CXK | 576 |
| 29 | AXB | 540 |
| 30 | Japan Airlines | 537 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 91918 |
| 2 | 🇪🇸 ES | 7516 |
| 3 | 🇮🇳 IN | 6813 |
| 4 | 🇦🇺 AU | 6520 |
| 5 | 🇧🇷 BR | 6038 |
| 6 | 🇩🇪 DE | 5866 |
| 7 | 🇮🇹 IT | 5846 |
| 8 | 🇨🇦 CA | 5725 |
| 9 | 🇯🇵 JP | 4967 |
| 10 | 🇬🇧 GB | 4670 |
| 11 | 🇫🇷 FR | 4371 |
| 12 | 🇨🇴 CO | 3759 |
| 13 | 🇲🇽 MX | 3266 |
| 14 | 🇬🇷 GR | 3111 |
| 15 | 🇳🇴 NO | 3024 |
| 16 | 🇨🇭 CH | 2809 |
| 17 | 🇲🇾 MY | 2385 |
| 18 | 🇹🇷 TR | 2146 |
| 19 | 🇿🇦 ZA | 1871 |
| 20 | 🇰🇷 KR | 1828 |
| 21 | 🇹🇭 TH | 1802 |
| 22 | 🇵🇱 PL | 1799 |
| 23 | 🇳🇿 NZ | 1796 |
| 24 | 🇵🇭 PH | 1597 |
| 25 | 🇬🇹 GT | 1568 |
| 26 | 🇲🇦 MA | 1203 |
| 27 | 🇲🇴 MO | 1148 |
| 28 | 🇳🇱 NL | 1074 |
| 29 | 🇲🇪 ME | 1061 |
| 30 | 🇭🇷 HR | 955 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2344 |
| 2 | Denver International Airport |  | US | 1846 |
| 3 | Tokyo International Airport |  | JP | 1646 |
| 4 | Indira Gandhi International Airport |  | IN | 1480 |
| 5 | Guaymaral Airport |  | CO | 1393 |
| 6 | Harry Reid International Airport |  | US | 1387 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1366 |
| 8 | Zurich Airport |  | CH | 1238 |
| 9 | Frankfurt am Main International Airport |  | DE | 1221 |
| 10 | La Aurora Airport |  | GT | 1207 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1168 |
| 12 | Macau International Airport |  | MO | 1148 |
| 13 | El Dorado International Airport |  | CO | 1134 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1092 |
| 15 | Chicago O'Hare International Airport |  | US | 1084 |
| 16 | Madrid Barajas International Airport |  | ES | 954 |
| 17 | Capua Airport |  | IT | 937 |
| 18 | Kuala Lumpur International Airport |  | MY | 935 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 926 |
| 20 | Salt Lake City International Airport |  | US | 923 |
| 21 | Charlotte/Douglas International Airport |  | US | 843 |
| 22 | Congonhas Airport |  | BR | 835 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 830 |
| 24 | Bengaluru International Airport |  | IN | 825 |
| 25 | Charles de Gaulle International Airport |  | FR | 824 |
| 26 | Malpensa International Airport |  | IT | 800 |
| 27 | Ninoy Aquino International Airport |  | PH | 734 |
| 28 | Daniel K Inouye International Airport |  | US | 731 |
| 29 | Tenerife Norte Airport |  | ES | 728 |
| 30 | General Edward Lawrence Logan International Airport |  | US | 724 |
| 31 | Barcelona International Airport |  | ES | 718 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 712 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 702 |
| 34 | Amsterdam Airport Schiphol |  | NL | 664 |
| 35 | Don Mueang International Airport |  | TH | 657 |
| 36 | Vitoria/Foronda Airport |  | ES | 649 |
| 37 | Calgary International Airport |  | CA | 642 |
| 38 | Seattle-Tacoma International Airport |  | US | 627 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 625 |
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
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 142 | 18m | 144 km | 353.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 141 | 20m | 250 km | 609.0 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 133 | 1h 1m | 695 km | 1,594.3 t |
| 25 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 133 | 44m | 241 km | 552.5 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 130 | 1h 43m | 1,423 km | 3,190.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 124 | 1h 17m | 961 km | 2,055.4 t |
| 29 | Calgary International Airport (CYYC) | Moose Jaw Municipal Airport (CJS4) | 122 | 1h 2m | 611 km | 1,286.7 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BPX278 | BPX | Daytona Beach International Airport (KDAB) | Skinners Wholesale Nursery Airport (16FD) | 2026-06-13 14:35 UTC | 2026-06-13 15:00 UTC | 24m |
| N80JF |  | Orange Municipal Airport (KORE) | Orange Municipal Airport (KORE) | 2026-06-13 14:39 UTC | 2026-06-13 14:54 UTC | 15m |
| TGEJR | TGE | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-06-13 14:43 UTC | 2026-06-13 14:53 UTC | 10m |
| N27DX |  | Republic Airport (KFRG) | Teterboro Airport (KTEB) | 2026-06-13 14:32 UTC | 2026-06-13 14:49 UTC | 17m |
| N722UE |  | North Las Vegas Airport (KVGT) | Sky Ranch Airport (K3L2) | 2026-06-13 14:34 UTC | 2026-06-13 14:47 UTC | 13m |
| SWR15Y | Swiss International | Melsbroek Air Base (EBMB) | Zurich Airport (LSZH) | 2026-06-13 13:42 UTC | 2026-06-13 14:38 UTC | 55m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-06-13 14:27 UTC | 2026-06-13 14:37 UTC | 9m |
| N87JF |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-06-13 13:52 UTC | 2026-06-13 14:35 UTC | 42m |
| SCA18 | SCA | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-06-13 14:15 UTC | 2026-06-13 14:33 UTC | 17m |
| N724GT |  | Raleigh-Durham International Airport (KRDU) | Orlando Executive Airport (KORL) | 2026-06-13 13:04 UTC | 2026-06-13 14:30 UTC | 1h 26m |
| N9114D |  | OI34 (OI34) | OI34 (OI34) | 2026-06-13 14:05 UTC | 2026-06-13 14:29 UTC | 23m |
| N380LA |  | Oak Glen Ranch Airport (3TS9) | Oak Glen Ranch Airport (3TS9) | 2026-06-13 14:11 UTC | 2026-06-13 14:28 UTC | 16m |
| N55428 |  | Knox County Airport (K4I3) | Licking County Regional Airport (KVTA) | 2026-06-13 14:11 UTC | 2026-06-13 14:27 UTC | 15m |
| SMGLR | SMG | Kbely Air Base (LKKB) | Kbely Air Base (LKKB) | 2026-06-13 14:07 UTC | 2026-06-13 14:24 UTC | 17m |
| THY77J | Turkish Airlines | Istanbul Airport (LTFM) | Nis Airport (LYNI) | 2026-06-13 13:39 UTC | 2026-06-13 14:24 UTC | 44m |
| WZZ9WL | Wizz Air | Memmingen Allgau Airport (EDJA) | Berane Airport (LYBR) | 2026-06-13 13:16 UTC | 2026-06-13 14:24 UTC | 1h 7m |
| CXK215 | CXK | Mckinney Ntl Airport (KTKI) | Nuggs Flying M Airport (TE68) | 2026-06-13 13:27 UTC | 2026-06-13 14:23 UTC | 56m |
| OOAAC | OOA | Antwerp International Airport (Deurne) (EBAW) | Antwerp International Airport (Deurne) (EBAW) | 2026-06-13 13:56 UTC | 2026-06-13 14:21 UTC | 24m |
| N267FG |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-06-13 12:58 UTC | 2026-06-13 14:21 UTC | 1h 23m |
| HB2473 |  | Sion Airport (LSGS) | Bex Airport (LSGB) | 2026-06-13 14:11 UTC | 2026-06-13 14:19 UTC | 7m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
