import React from 'react';
import ResponsiveAntMenu from './ResponsiveAntMenu'
import { Menu } from 'antd';

const Nav = () => (
    <ResponsiveAntMenu
        mobileMenuContent={isMenuShown => isMenuShown ? <button>Close</button> : <button>Open</button>}
        menuClassName={'responsive-ant-menu'}
    >
        {(onLinkClick) =>
            <Menu>
                <Menu.Item key='/' className={'menu-home'}>
                    <a onClick={onLinkClick} href={'/'}>Stanford | Engineering</a>
                </Menu.Item>
            </Menu>
        }
    </ResponsiveAntMenu>
);

export default Nav;