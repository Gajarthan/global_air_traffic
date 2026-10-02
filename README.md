# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--02_02:16:59_UTC-green)

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

**Latest saved flight:** 2026-10-02 02:16:59 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-10-02 02:16:59 UTC

- **274,293** saved flights
- **80,014** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **274,293** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,319,209.0 tonnes** estimated CO2 emissions
- **192,417,911 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10763 |
| 2 | SkyWest Airlines | 9544 |
| 3 | EJA | 5372 |
| 4 | IndiGo | 4568 |
| 5 | American Airlines | 4252 |
| 6 | Southwest Airlines | 4033 |
| 7 | Delta Air Lines | 3404 |
| 8 | ENY | 3212 |
| 9 | LATAM Airlines | 2651 |
| 10 | AZU | 2581 |
| 11 | Vueling | 2275 |
| 12 | WIF | 2231 |
| 13 | LXJ | 2164 |
| 14 | Lufthansa | 2068 |
| 15 | easyJet | 1823 |
| 16 | Swiss International | 1794 |
| 17 | QLK | 1774 |
| 18 | EJU | 1708 |
| 19 | AXM | 1686 |
| 20 | United Airlines | 1674 |
| 21 | Alaska Airlines | 1616 |
| 22 | All Nippon Airways | 1567 |
| 23 | PGT | 1543 |
| 24 | GLO | 1533 |
| 25 | WMT | 1528 |
| 26 | Air France | 1505 |
| 27 | VIV | 1504 |
| 28 | Wizz Air | 1484 |
| 29 | CXK | 1355 |
| 30 | AEE | 1308 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 228813 |
| 2 | 🇪🇸 ES | 17142 |
| 3 | 🇧🇷 BR | 16110 |
| 4 | 🇦🇺 AU | 15850 |
| 5 | 🇨🇦 CA | 15302 |
| 6 | 🇮🇹 IT | 14790 |
| 7 | 🇮🇳 IN | 14461 |
| 8 | 🇩🇪 DE | 13131 |
| 9 | 🇨🇴 CO | 12711 |
| 10 | 🇬🇧 GB | 12628 |
| 11 | 🇫🇷 FR | 10852 |
| 12 | 🇯🇵 JP | 10468 |
| 13 | 🇹🇷 TR | 8291 |
| 14 | 🇬🇷 GR | 7884 |
| 15 | 🇲🇽 MX | 7581 |
| 16 | 🇨🇭 CH | 7272 |
| 17 | 🇳🇴 NO | 6762 |
| 18 | 🇹🇭 TH | 4911 |
| 19 | 🇲🇾 MY | 4565 |
| 20 | 🇿🇦 ZA | 4553 |
| 21 | 🇵🇱 PL | 4476 |
| 22 | 🇳🇿 NZ | 3878 |
| 23 | 🇵🇭 PH | 3619 |
| 24 | 🇬🇹 GT | 3438 |
| 25 | 🇭🇷 HR | 3119 |
| 26 | 🇰🇷 KR | 3088 |
| 27 | 🇲🇦 MA | 2711 |
| 28 | 🇲🇪 ME | 2572 |
| 29 | 🇳🇱 NL | 2454 |
| 30 | 🇮🇩 ID | 2270 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5571 |
| 2 | Denver International Airport |  | US | 4475 |
| 3 | Indira Gandhi International Airport |  | IN | 3272 |
| 4 | Tokyo International Airport |  | JP | 3138 |
| 5 | El Dorado International Airport |  | CO | 3024 |
| 6 | Harry Reid International Airport |  | US | 2952 |
| 7 | Guaymaral Airport |  | CO | 2845 |
| 8 | Zurich Airport |  | CH | 2844 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2743 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2624 |
| 11 | La Aurora Airport |  | GT | 2613 |
| 12 | Salt Lake City International Airport |  | US | 2435 |
| 13 | Congonhas Airport |  | BR | 2342 |
| 14 | Chicago O'Hare International Airport |  | US | 2322 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2246 |
| 16 | Capua Airport |  | IT | 2128 |
| 17 | Madrid Barajas International Airport |  | ES | 2108 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2086 |
| 19 | Frankfurt am Main International Airport |  | DE | 2064 |
| 20 | Enrique Olaya Herrera Airport |  | CO | 1959 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1946 |
| 22 | Malpensa International Airport |  | IT | 1943 |
| 23 | Charles de Gaulle International Airport |  | FR | 1941 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1929 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1834 |
| 26 | Macau International Airport |  | MO | 1789 |
| 27 | Ninoy Aquino International Airport |  | PH | 1779 |
| 28 | Charlotte/Douglas International Airport |  | US | 1715 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1702 |
| 30 | Barcelona International Airport |  | ES | 1693 |
| 31 | Viracopos International Airport |  | BR | 1644 |
| 32 | Kuala Lumpur International Airport |  | MY | 1634 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1614 |
| 34 | Seattle-Tacoma International Airport |  | US | 1608 |
| 35 | Calgary International Airport |  | CA | 1560 |
| 36 | Don Mueang International Airport |  | TH | 1550 |
| 37 | Vancouver International Airport |  | CA | 1538 |
| 38 | Oslo Gardermoen Airport |  | NO | 1534 |
| 39 | Bengaluru International Airport |  | IN | 1533 |
| 40 | Reno/Tahoe International Airport |  | US | 1487 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1132 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1032 | 21m | 244 km | 4,345.5 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 767 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 694 | 1h 6m | 770 km | 9,219.3 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 689 | 24m | 225 km | 2,673.0 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 605 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 458 | 44m | 555 km | 4,385.6 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 441 | 27m | 275 km | 2,089.7 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 433 | 1h 50m | 1,423 km | 10,626.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 421 | 44m | 241 km | 1,748.7 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 392 | 24m | 218 km | 1,476.8 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 382 | 35m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 372 | 23m | 55 km | 353.6 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 370 | 21m | 250 km | 1,598.2 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 352 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 347 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 343 | 1h 6m | 706 km | 4,176.0 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 343 | 19m | 99 km | 587.5 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 342 | 26m | 215 km | 1,266.6 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 336 | 1h 39m | 1,156 km | 6,703.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 318 | 19m | 144 km | 791.0 t |
| 22 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 314 | 18m | 14 km | 78.5 t |
| 23 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 311 | 1h 14m | 961 km | 5,155.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 305 | 42m | 535 km | 2,816.9 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 296 | 1h 50m | 1,304 km | 6,659.2 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 273 | 15m | 154 km | 723.3 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 273 | 51m | 556 km | 2,616.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N61KM |  | Hunter Army Air Field (KSVN) | Savannah/Hilton Head International Airport (KSAV) | 2026-10-02 01:58 UTC | 2026-10-02 02:16 UTC | 18m |
| BURNY10 | BUR | Kickapoo Downtown Airport (KCWC) | 5TA4 (5TA4) | 2026-10-02 01:56 UTC | 2026-10-02 02:15 UTC | 18m |
| BOX531 | BOX | Suvarnabhumi Airport (VTBS) | Naypyidaw Airport (VYEL) | 2026-10-02 01:14 UTC | 2026-10-02 02:10 UTC | 56m |
| KSF8 | KSF | Kent State University Airport (K1G3) | Beaver County Airport (KBVI) | 2026-10-02 01:15 UTC | 2026-10-02 02:08 UTC | 53m |
| N48EF |  | Whiteman Airport (KWHP) | Whiteman Airport (KWHP) | 2026-10-02 01:34 UTC | 2026-10-02 02:02 UTC | 27m |
| R21230 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-10-02 00:13 UTC | 2026-10-02 02:00 UTC | 1h 46m |
| N269DD |  | Whiteman Airport (KWHP) | Whiteman Airport (KWHP) | 2026-10-02 01:06 UTC | 2026-10-02 01:59 UTC | 52m |
| CAI6CP | CAI | Nuremberg Airport (EDDN) | Nis Airport (LYNI) | 2026-10-02 00:21 UTC | 2026-10-02 01:56 UTC | 1h 34m |
| BRG2652 | BRG | Ralph Wien Memorial Airport (PAOT) | Selawik Airport (PASK) | 2026-10-02 01:27 UTC | 2026-10-02 01:53 UTC | 26m |
| N80585 |  | Harford County Airport (K0W3) | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | 2026-10-02 00:36 UTC | 2026-10-02 01:52 UTC | 1h 16m |
| ARCAS05 | ARC | Kickapoo Downtown Airport (KCWC) | Abilene Executive Airpark (TX00) | 2026-10-02 01:28 UTC | 2026-10-02 01:42 UTC | 14m |
| N377PL |  | Mc Clellan-Palomar Airport (KCRQ) | Fairbanks Airfield (1ID7) | 2026-10-01 23:49 UTC | 2026-10-02 01:40 UTC | 1h 50m |
| VWA118 | VWA | Falcon Field (KFFZ) | Pinal Airpark (KMZJ) | 2026-10-02 01:01 UTC | 2026-10-02 01:40 UTC | 38m |
| N570FG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-10-02 00:44 UTC | 2026-10-02 01:34 UTC | 49m |
| N560ZF |  | Boise Air Trml/Gowen Field (KBOI) | Mineta San Jose International Airport (KSJC) | 2026-10-01 23:59 UTC | 2026-10-02 01:32 UTC | 1h 32m |
| BURNY02 | BUR | Kickapoo Downtown Airport (KCWC) | 5TA4 (5TA4) | 2026-10-02 01:12 UTC | 2026-10-02 01:31 UTC | 19m |
| NYT301 | NYT | Tribhuvan International Airport (VNKT) | Langtang Airport (VNLT) | 2026-10-02 01:24 UTC | 2026-10-02 01:31 UTC | 7m |
| AM712 |  | Launceston Airport (YMLT) | Devonport Airport (YDPO) | 2026-10-02 01:14 UTC | 2026-10-02 01:28 UTC | 13m |
| VTASC | VTA | Bharkot Airport (VI82) | Bharkot Airport (VI82) | 2026-10-02 01:12 UTC | 2026-10-02 01:28 UTC | 15m |
| TKR01 | TKR | Mountain Valley Airport (KL94) | 6CL4 (6CL4) | 2026-10-02 00:54 UTC | 2026-10-02 01:26 UTC | 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
